# Uso local del sitio

| Campo | Valor |
|--------|--------|
| Rol | 🛠️ HOWTO de build / publicación (no es norma) |

> [!NOTE]
> Look Material alineado con **sdaf-core** (Decisión A). Fuentes del sitio: la raíz del repo (`docs_dir: ..`), mismo modelo que sdaf-core. No hacen falta symlinks.

## En esta página

- [Requisitos](#requisitos)
- [Comandos exactos en Windows con PowerShell](#comandos-exactos-en-windows-con-powershell)
- [Checks del CI en local](#checks-del-ci-en-local)
- [Publicación versionada (mike, igual que sdaf-core)](#publicación-versionada-mike-igual-que-sdaf-core)
- [Convenciones de bloques de código](#convenciones-de-bloques-de-código)
- [Fuente única (sin wrappers)](#fuente-única-sin-wrappers)
- [Relacionado](#relacionado)

## Requisitos

- Python 3.11+ y `pip`.
- PowerShell 5.1+ (Windows) o `pwsh` para el checker de enlaces.

## Comandos exactos en Windows con PowerShell

```powershell
# Desde la raíz del repo (sdaf-stack-dotnet/)
py -m venv .venv
.venv\Scripts\Activate.ps1

pip install -r requirements-docs.txt

# Servidor local con recarga en caliente -> http://127.0.0.1:8000
mkdocs serve -f mkdocs/mkdocs.yml

# Build de producción (mismo comando que corre el CI). site_dir sale del
# docs_dir: por defecto /tmp/sdaf-stack-dotnet-mkdocs-site; cámbialo con MKDOCS_SITE_DIR.
mkdocs build -f mkdocs/mkdocs.yml --strict
```

> [!TIP]
> `mkdocs build -f mkdocs/mkdocs.yml --strict` convierte en error cualquier warning (enlace roto, snippet inexistente, página fuera del `nav`). Ejecútalo antes de abrir PR sobre docs o contratos.

## Checks del CI en local

Los mismos que ejecutan [`validate.yml`](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/blob/main/.github/workflows/validate.yml) y [`docs-links.yml`](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/blob/main/.github/workflows/docs-links.yml) (salvo markdownlint, que necesita Node). Los dos últimos usan un checkout de sdaf-core `v0.4.2` al lado de este repo (`../sdaf-core`).

```powershell
pip install pyyaml jsonschema

# Coherencia pack.yaml ↔ cabeceras ↔ historial ↔ citas skill@version ↔ examples
python scripts/check-pack-metadata.py
python scripts/test-check-pack-metadata.py

# Historial solo crece respecto a la rama base
python scripts/check-history-append-only.py --base origin/main

# Enlaces, anclas (GitHub y MkDocs) y huérfanos
powershell -File ./scripts/check-md-links.ps1 -StrictAnchors -StrictOrphans

# Escenarios y worklogs con los validadores del core
python ../sdaf-core/scripts/validate-config.py --strict-i4 --consumer-root . examples/01-pack-only.yaml examples/02-pack-frontend.yaml
python ../sdaf-core/scripts/validate-worklog.py worklogs/INIT-auditoria-v0.2.0/Iteration-001.md
```

## Publicación versionada (mike, igual que sdaf-core)

El CI publica con [`mike`](https://github.com/jimporter/mike) a la rama `gh-pages`:

| Evento | Alias | URL |
|--------|-------|-----|
| push a `main` | `dev` | https://cyberdine-systems-corporation.github.io/sdaf-stack-dotnet/dev/ |
| tag `vX.Y.Z` | `X.Y` + `latest` | `…/sdaf-stack-dotnet/X.Y/` (default → `latest`) |

En GitHub → **Settings → Pages**, Source debe ser **Deploy from a branch** → rama **`gh-pages`** / `(root)` — no "GitHub Actions". Es el mismo modelo que `sdaf-core`.

## Convenciones de bloques de código

El resaltado de sintaxis (Pygments vía `pymdownx.highlight`) cubre, entre otros, YAML, PowerShell, Bash, Markdown, C#, SQL y JSON.

## Fuente única (sin wrappers)

Agentes, skills, playbooks, prompts y `ADOPT.md` se sirven **directamente** desde su ruta en el repo. `mkdocs.yml` excluye el tooling (`mkdocs/`, `scripts/`, `site/`) y deja `worklogs/` fuera del `nav`. No hay páginas espejo en `docs/` que re-incluyan el cuerpo con snippets.

Los YAML de `examples/` sí se incrustan en [Escenarios](adoption/escenarios.md) con `pymdownx.snippets`.

## Relacionado

| | Destino | Por qué |
|--|---------|---------|
| 🧭 | [README.md](../README.md) | Hub del sitio / tres puertas |
| 🧭 | [Navegación](navegacion-docs.md) | Vocabulario visual y Decisión A |
| 📝 | [Checklist de página](checklist-pagina-docs.md) | DoD de PRs de docs |
| 🛠️ | [CONTRIBUTING.md](../CONTRIBUTING.md) | Flujo de PR y worklog |
| 🛠️ | [.github/workflows/docs.yml](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/blob/main/.github/workflows/docs.yml) | Mismo build en CI |
| 🧭 | [mkdocs/README.md](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/blob/main/mkdocs/README.md) | Layout del sitio Material |
