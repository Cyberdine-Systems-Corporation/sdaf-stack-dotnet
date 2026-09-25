# Contribuir a sdaf-stack-dotnet

| Campo | Valor |
|--------|--------|
| Rol | 🛠️ HOWTO de contribución (no es norma del método) |

> [!NOTE]
> La norma vive en **sdaf-core** (línea `0.4.x`). Esta página solo explica cómo aplicarla a este pack.

## En esta página

- [Flujo](#flujo)
- [Clase del cambio y versión](#clase-del-cambio-y-versión)
- [Historial y fechas](#historial-y-fechas)
- [Worklog](#worklog)
- [Checks](#checks)
- [Relacionado](#relacionado)

## Flujo

1. Rama desde `main` (`feat/…`, `fix/…`, `docs/…`); nunca commit directo a `main`.
2. PR con la plantilla `.github/pull_request_template.md` rellenada (GitHub la carga sola).
3. CI verde: `validate`, `Docs links` y `docs`.
4. QG-Review: aprueba la identidad de [`CODEOWNERS`](CODEOWNERS). Con un solo mantenedor puede aprobar su propio PR (H13 §7 del core).
5. Merge humano. Un agente no hace merge, auto-merge, push, tag ni release sin orden humana explícita en el encargo vigente (H06 §7 del core).

Commits con prefijo (`feat:`, `fix:`, `docs:`, `chore:`) y prosa en castellano.

## Clase del cambio y versión

| Clase | Qué cambia | Versión |
|-------|------------|---------|
| Redacción | Claridad, TOC, Relacionado, enlaces; la obligación no cambia | patch del artefacto; historial «Sin cambio de norma» |
| Significado | Cambia una obligación de un contrato, skill o playbook Approved | minor del artefacto; entrada en [CHANGELOG](CHANGELOG.md) |
| Compat | Cambia el rango `sdaf_core` de [`pack.yaml`](pack.yaml) | minor del pack (0.x); upgrade en [ADOPT](ADOPT.md#upgrade) |

`pack.yaml` es la fuente de verdad: su `version` coincide con las citas `skill@version`, el campo `Pack` de cada cabecera y `stack.pack` de `examples/`. Un release del pack alinea todos los artefactos a esa versión, como en 0.2.0 y 0.3.0.

## Historial y fechas

- Cambio de versión = fila nueva al final de **Historial**. Las filas publicadas no se editan ni se borran (H08 §7 del core).
- Fechas nuevas en ISO 8601 con hora y zona: `AAAA-MM-DDThh:mm±hh:mm`, hora medida al registrar el cambio (H13 §9). Las publicadas hasta `v0.2.0` conservan el día.
- La `Fecha` de cabecera es la de la fila más reciente de la versión máxima.

## Worklog

Cambio material (contrato, skill, playbook, prompt o ADR del pack): worklog en `worklogs/<PBI>/Iteration-NNN.md` con el frontmatter de `templates/worklog.md` del core `v0.4.0`. `commit`, `pr` y `sha` quedan en `null` si aún no existen. Typos y enlaces: no obligatorio.

## Checks

Los mismos que el CI, en local: ver [uso local](docs/uso-local.md#checks-del-ci-en-local). Resumen:

| Check | Qué falla |
|-------|-----------|
| `check-pack-metadata.py` | Versión, `Pack`, fechas o citas `skill@version` que no cuadran con `pack.yaml` |
| `check-history-append-only.py` | Fila de historial o sección del CHANGELOG borrada o reescrita |
| `check-md-links.ps1 -StrictAnchors -StrictOrphans` | Enlace, ancla (GitHub y MkDocs) o página huérfana |
| `validate-sdaf` (action del core) | `examples/` fuera del schema o de las invariantes |
| `validate-worklog.py` (core) | Worklog con frontmatter inválido |
| markdownlint | Fences sin lenguaje (MD040) y enlaces vacíos (MD042) |
| `mkdocs build --strict` | Nav, enlaces o snippets rotos en el sitio |

## Relacionado

| | Destino | Por qué |
|--|---------|---------|
| 🧭 | [README.md](README.md) | Hub del pack |
| 📝 | [Checklist de página](docs/checklist-pagina-docs.md) | DoD de PRs de markdown |
| 🛠️ | [Uso local](docs/uso-local.md) | Build y checks en local |
| 🧭 | [SECURITY.md](SECURITY.md) | Aviso de vulnerabilidades |
