#Requires -Version 5.1
<#
.SYNOPSIS
  Valida enlaces relativos, anclas y huerfanos en el Markdown del repo.

.DESCRIPTION
  Exit 1 si un enlace relativo apunta a un archivo inexistente.
  Anclas: deben existir con el slug de GitHub (github-slugger) Y con el de
  MkDocs (slugify_unicode de mkdocs/mkdocs.yml); el sitio sirve las mismas
  paginas. Por defecto es aviso; -StrictAnchors lo convierte en error.
  Huerfanos (.md sin enlaces entrantes desde otro .md): aviso por defecto;
  -StrictOrphans lo convierte en error. README.md raiz y .github/ se omiten.
  Ignora http(s), mailto y ftp. No recorre .git, .venv, site, mkdocs/ (tooling;
  mkdocs.yml lo excluye del sitio) ni .sdaf-core (checkout del core en CI).

.EXAMPLE
  pwsh -File ./scripts/check-md-links.ps1 -StrictAnchors -StrictOrphans
  powershell -File ./scripts/check-md-links.ps1
#>
[CmdletBinding()]
param(
    [string]$Root = '',
    [switch]$StrictAnchors,
    [switch]$StrictOrphans
)

$ErrorActionPreference = 'Stop'
if ([string]::IsNullOrWhiteSpace($Root)) {
    $scriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
    $Root = (Resolve-Path (Join-Path $scriptDir '..')).Path
}
$Root = $Root.TrimEnd('\', '/')
$failCount = 0
$warnCount = 0
$skipDirs = '[\\/](\.git|\.venv|venv|site|node_modules|\.sdaf-core)[\\/]'
$mdFiles = Get-ChildItem -Path $Root -Filter '*.md' -Recurse -File |
    Where-Object {
        $rel = $_.FullName.Substring($Root.Length)
        $rel -notmatch $skipDirs -and $rel -notmatch '^[\\/]mkdocs[\\/]'
    }

function Get-RelPath([string]$Full) {
    return $Full.Substring($Root.Length).TrimStart('\', '/').Replace('\', '/')
}

# Texto visible del heading: sin code spans, enlaces ni enfasis.
function Get-HeadingText([string]$Raw) {
    $s = $Raw.Trim() -replace '\s+#+\s*$', ''
    $s = [regex]::Replace($s, '!?\[([^\]]*)\]\([^)]*\)', '$1')
    $s = $s -replace '`', ''
    $s = $s -replace '(\*\*|__)', ''
    return $s
}

# github-slugger: minusculas; quita lo que no sea letra, marca, numero,
# conector, espacio o guion; cada espacio pasa a guion (sin colapsar).
function Get-GfmSlug([string]$Text) {
    $s = $Text.ToLowerInvariant()
    $s = [regex]::Replace($s, '[^\p{L}\p{M}\p{N}\p{Pc} \-]', '')
    return $s.Replace(' ', '-')
}

# markdown.extensions.toc.slugify_unicode: quita lo que no sea \w, espacio o
# guion; strip; minusculas; colapsa espacios y guiones en un guion.
function Get-MkDocsSlug([string]$Text) {
    $s = [regex]::Replace($Text, '[^\p{L}\p{N}_\s\-]', '').Trim().ToLowerInvariant()
    return [regex]::Replace($s, '[\-\s]+', '-')
}

$slugCache = @{}
function Get-Slugs([string]$FilePath) {
    if ($slugCache.ContainsKey($FilePath)) { return $slugCache[$FilePath] }
    $gfm = @{}; $mk = @{}
    $inFence = $false
    foreach ($line in (Get-Content -LiteralPath $FilePath -Encoding UTF8)) {
        if ($line -match '^\s*(```|~~~)') { $inFence = -not $inFence; continue }
        if ($inFence) { continue }
        if ($line -match '^(#{1,6})\s+(.+)$') {
            $text = Get-HeadingText $Matches[2]
            foreach ($pair in @(@($gfm, (Get-GfmSlug $text), '-'), @($mk, (Get-MkDocsSlug $text), '_'))) {
                $map = $pair[0]; $slug = $pair[1]; $sep = $pair[2]
                if ($map.ContainsKey($slug)) {
                    $n = 1
                    while ($map.ContainsKey("$slug$sep$n")) { $n++ }
                    $slug = "$slug$sep$n"
                }
                $map[$slug] = $true
            }
        }
    }
    $slugCache[$FilePath] = @{ Gfm = $gfm; MkDocs = $mk }
    return $slugCache[$FilePath]
}

function Test-Anchor([string]$FilePath, [string]$Anchor, [string]$From, [string]$Target) {
    $slugs = Get-Slugs $FilePath
    $a = [Uri]::UnescapeDataString($Anchor).ToLowerInvariant()
    $missing = @()
    if (-not $slugs.Gfm.ContainsKey($a)) { $missing += 'GitHub' }
    if (-not $slugs.MkDocs.ContainsKey($a)) { $missing += 'MkDocs' }
    if ($missing.Count -gt 0) {
        $msg = "ANCHOR missing ($($missing -join ', ')): $From -> $Target"
        if ($StrictAnchors) {
            Write-Host "BROKEN: $msg" -ForegroundColor Red
            $script:failCount++
        } else {
            Write-Warning $msg
            $script:warnCount++
        }
    }
}

$linkPattern = '\[([^\]]*)\]\(([^)\s]+)(?:\s+"[^"]*")?\)'
$inbound = @{}
foreach ($f in $mdFiles) { $inbound[(Get-RelPath $f.FullName)] = 0 }

foreach ($file in $mdFiles) {
    $dir = $file.DirectoryName
    $from = Get-RelPath $file.FullName
    $content = Get-Content -LiteralPath $file.FullName -Raw -Encoding UTF8
    if ([string]::IsNullOrEmpty($content)) { continue }
    # Los bloques de codigo no son enlaces.
    $content = [regex]::Replace($content, '(?ms)^\s*(```|~~~).*?^\s*\1', '')

    foreach ($m in [regex]::Matches($content, $linkPattern)) {
        $target = $m.Groups[2].Value.Trim()
        if ($target -match '^(https?:|mailto:|ftp:)') { continue }

        if ($target.StartsWith('#')) {
            Test-Anchor $file.FullName $target.Substring(1) $from $target
            continue
        }

        $pathPart = $target
        $anchor = $null
        $idx = $target.IndexOf('#')
        if ($idx -ge 0) {
            $pathPart = $target.Substring(0, $idx)
            $anchor = $target.Substring($idx + 1)
        }
        if ([string]::IsNullOrWhiteSpace($pathPart)) { continue }

        $pathPart = [Uri]::UnescapeDataString($pathPart)
        $resolved = [System.IO.Path]::GetFullPath((Join-Path $dir $pathPart))

        if (-not (Test-Path -LiteralPath $resolved)) {
            Write-Host "BROKEN: $from -> $target (missing file)" -ForegroundColor Red
            $failCount++
            continue
        }

        $item = Get-Item -LiteralPath $resolved -Force
        $isMd = ($item -is [System.IO.FileInfo]) -and $resolved.EndsWith('.md', [StringComparison]::OrdinalIgnoreCase)
        if ($isMd -and $resolved.StartsWith($Root)) {
            $destRel = Get-RelPath $resolved
            if ($inbound.ContainsKey($destRel) -and $destRel -ne $from) { $inbound[$destRel]++ }
        }

        if ($anchor) {
            if ($isMd) {
                Test-Anchor $resolved $anchor $from $target
            } else {
                Write-Warning "ANCHOR skipped (not markdown): $from -> $target"
                $warnCount++
            }
        }
    }
}

foreach ($key in ($inbound.Keys | Sort-Object)) {
    if ($key -eq 'README.md' -or $key.StartsWith('.github/')) { continue }
    if ($inbound[$key] -eq 0) {
        $msg = "ORPHAN: $key (no inbound relative links from other .md)"
        if ($StrictOrphans) {
            Write-Host "BROKEN: $msg" -ForegroundColor Red
            $failCount++
        } else {
            Write-Warning $msg
            $warnCount++
        }
    }
}

Write-Host "check-md-links: files=$($mdFiles.Count) failures=$failCount warnings=$warnCount"
if ($failCount -gt 0) {
    exit 1
}
exit 0
