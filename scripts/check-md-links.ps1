#Requires -Version 5.1
<#
.SYNOPSIS
  Valida enlaces relativos en Markdown del repo.

.DESCRIPTION
  Exit 1 si un enlace relativo apunta a un archivo inexistente.
  Warnings para anclas no encontradas y .md huérfanos (sin inbound).
  Ignora http(s), mailto, anchors-only (#...).

.EXAMPLE
  pwsh -File ./scripts/check-md-links.ps1
  powershell -File ./scripts/check-md-links.ps1
#>
[CmdletBinding()]
param(
    [string]$Root = ''
)

$ErrorActionPreference = 'Stop'
if ([string]::IsNullOrWhiteSpace($Root)) {
    $scriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
    $Root = (Resolve-Path (Join-Path $scriptDir '..')).Path
}
$failCount = 0
$warnCount = 0
$mdFiles = Get-ChildItem -Path $Root -Filter '*.md' -Recurse -File |
    Where-Object { $_.FullName -notmatch '[\\/]\.git[\\/]' }

function Get-GfmSlug {
    param([string]$Heading)
    $s = $Heading.Trim()
    $s = $s -replace '^#+\s+', ''
    $s = $s -replace '\s+', '-'
    $s = $s.ToLowerInvariant()
    $s = [regex]::Replace($s, '[^\p{L}\p{Nd}_-]', '')
    return $s
}

function Get-HeadingsMap {
    param([string]$FilePath)
    $map = @{}
    $lines = Get-Content -LiteralPath $FilePath -Encoding UTF8
    foreach ($line in $lines) {
        if ($line -match '^(#{1,6})\s+(.+)$') {
            $slug = Get-GfmSlug $Matches[2]
            if (-not $map.ContainsKey($slug)) { $map[$slug] = 0 }
            $map[$slug]++
        }
    }
    return $map
}

$linkPattern = '\[([^\]]*)\]\(([^)]+)\)'
$inbound = @{}
foreach ($f in $mdFiles) {
    $rel = $f.FullName.Substring($Root.Length).TrimStart('\', '/').Replace('\', '/')
    $inbound[$rel] = 0
}

foreach ($file in $mdFiles) {
    $dir = $file.DirectoryName
    $content = Get-Content -LiteralPath $file.FullName -Raw -Encoding UTF8
    if ([string]::IsNullOrEmpty($content)) { continue }

    $regexMatches = [regex]::Matches($content, $linkPattern)
    $selfHeadings = $null
    foreach ($m in $regexMatches) {
        $target = $m.Groups[2].Value.Trim()
        if ($target -match '^(https?:|mailto:|ftp:)') { continue }

        if ($target.StartsWith('#')) {
            if ($null -eq $selfHeadings) { $selfHeadings = Get-HeadingsMap $file.FullName }
            $slug = $target.Substring(1).ToLowerInvariant()
            if (-not $selfHeadings.ContainsKey($slug)) {
                $from = $file.FullName.Substring($Root.Length).TrimStart('\', '/')
                Write-Warning "ANCHOR missing: $from -> $target (same file)"
                $warnCount++
            }
            continue
        }

        $pathPart = $target
        $anchor = $null
        if ($target.Contains('#')) {
            $idx = $target.IndexOf('#')
            $pathPart = $target.Substring(0, $idx)
            $anchor = $target.Substring($idx + 1)
        }
        if ([string]::IsNullOrWhiteSpace($pathPart)) { continue }

        $pathPart = [Uri]::UnescapeDataString($pathPart)
        $resolved = [System.IO.Path]::GetFullPath((Join-Path $dir $pathPart))

        if (-not (Test-Path -LiteralPath $resolved)) {
            $from = $file.FullName.Substring($Root.Length).TrimStart('\', '/')
            Write-Host "BROKEN: $from -> $target (missing file)" -ForegroundColor Red
            $failCount++
            continue
        }

        $item = Get-Item -LiteralPath $resolved
        if (($item -is [System.IO.FileInfo]) -and $resolved.EndsWith('.md', [StringComparison]::OrdinalIgnoreCase)) {
            $destRel = $resolved.Substring($Root.Length).TrimStart('\', '/').Replace('\', '/')
            if ($inbound.ContainsKey($destRel)) {
                $inbound[$destRel]++
            }
        }

        if ($anchor) {
            if ($item -is [System.IO.DirectoryInfo]) {
                Write-Warning "ANCHOR skipped (directory link): $($file.Name) -> $target"
                $warnCount++
                continue
            }
            if ($resolved.EndsWith('.md', [StringComparison]::OrdinalIgnoreCase)) {
                $headings = Get-HeadingsMap $resolved
                $slug = $anchor.ToLowerInvariant()
                if (-not $headings.ContainsKey($slug)) {
                    $from = $file.FullName.Substring($Root.Length).TrimStart('\', '/')
                    Write-Warning "ANCHOR missing: $from -> #$anchor in $pathPart"
                    $warnCount++
                }
            }
        }
    }
}

foreach ($key in ($inbound.Keys | Sort-Object)) {
    if ($key -eq 'README.md') { continue }
    if ($inbound[$key] -eq 0) {
        Write-Warning "ORPHAN: $key (no inbound relative links from other .md)"
        $warnCount++
    }
}

Write-Host "check-md-links: files=$($mdFiles.Count) failures=$failCount warnings=$warnCount"
if ($failCount -gt 0) {
    exit 1
}
exit 0
