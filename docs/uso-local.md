# Uso local del sitio

| Campo | Valor |
|--------|--------|
| Rol | 🛠️ HOWTO de build / publicación (no es norma) |

> [!NOTE]
> Look Material alineado con **sdaf-core** (Decisión A). Fuentes del sitio: symlinks en `mkdocs/src/` hacia el árbol canónico (mismo modelo que sdaf-core).

## Requisitos

- Python 3.11+ y `pip`.
- En Windows, para que los symlinks de `mkdocs/src/` se materialicen al clonar: [Developer Mode](https://learn.microsoft.com/windows/apps/get-started/enable-your-device-for-development) o `git clone` con permisos de symlink (`core.symlinks=true`).

## Comandos exactos (Windows / PowerShell)

```powershell
# Desde la raíz del repo (sdaf-stack-dotnet/)
py -m venv .venv
.venv\Scripts\Activate.ps1

pip install -r requirements-docs.txt

# Servidor local con recarga en caliente -> http://127.0.0.1:8000
mkdocs serve -f mkdocs/mkdocs.yml

# Build de producción a ./site (mismo comando que corre el CI en PRs)
mkdocs build -f mkdocs/mkdocs.yml --strict
```

> [!TIP]
> `mkdocs build -f mkdocs/mkdocs.yml --strict` convierte en error cualquier warning (enlace roto, snippet inexistente, página fuera del `nav`). Ejecútalo antes de abrir PR sobre docs o contratos.

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

Agentes, skills, playbooks, prompts y `ADOPT.md` se sirven **directamente** desde la raíz del repo (symlinks en `mkdocs/src/`). No hay páginas espejo en `docs/` que re-incluyan el cuerpo con snippets.

Los YAML de `examples/` sí se incrustan en [Escenarios](adoption/escenarios.md) con `pymdownx.snippets`.

## Relacionado

| | Destino | Por qué |
|--|---------|---------|
| 🧭 | [README.md](../README.md) | Hub del sitio / tres puertas |
| 🧭 | [Navegación](navegacion-docs.md) | Vocabulario visual y Decisión A |
| 📝 | [Checklist de página](checklist-pagina-docs.md) | DoD de PRs de docs |
| 🛠️ | [.github/workflows/docs.yml](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/blob/main/.github/workflows/docs.yml) | Mismo build en CI |
| 🧭 | [mkdocs/README.md](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/blob/main/mkdocs/README.md) | Layout del sitio Material |
