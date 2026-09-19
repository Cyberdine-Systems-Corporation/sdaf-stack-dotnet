# Changelog — sdaf-stack-dotnet

Formato basado en [Keep a Changelog](https://keepachangelog.com/). El semver del pack vive en [`pack.yaml`](pack.yaml).

## [Unreleased]

### Changed

- Docs MkDocs **Decisión A** (paridad visual con sdaf-core): sin `primary` indigo, features Material mínimas, `slugify_unicode`, `pymdownx.blocks.admonition`, deps sin `git-revision-date-localized`.
- Hub del sitio: tres puertas con vocabulario emoji cerrado (sin `:material-*`).
- **Fase 3:** sitio en `mkdocs/` con symlinks a fuentes canónicas (como sdaf-core); eliminados wrappers `docs/agents|skills|playbooks` basados en snippets.
- Nav del sitio incluye **Prompts**; Relacionado con columna de icono en contratos, skills, playbooks y prompts.

### Added

- [`docs/checklist-pagina-docs.md`](docs/checklist-pagina-docs.md) — DoD de página markdown (adaptado del core al overlay).
- [`agents/README.md`](agents/README.md) y [`playbooks/README.md`](playbooks/README.md) — índices canónicos del overlay.
- [`.github/pull_request_template.md`](.github/pull_request_template.md) — DoD de PR enlaza el checklist de página.

## [0.1.1] — 2026-09-17

### Changed

- Alineación de semver del pack a **0.1.1** (`pack.yaml`, ADOPT pin `v0.1.1`, `examples/`, citas `skill@version` y campo Pack en agents/prompts/playbooks/skills).
- UX de documentación GFM: hub de tres puertas en README, TOC **En esta página**, cierre **Relacionado**, Mermaid con clases semánticas, alertas GFM.

### Added

- [`docs/navegacion-docs.md`](docs/navegacion-docs.md) — vocabulario visual y mapa de clics.
- [`scripts/check-md-links.ps1`](scripts/check-md-links.ps1) — checker de enlaces relativos.
- [`.github/workflows/docs-links.yml`](.github/workflows/docs-links.yml) — CI del checker.

### Notas

- Responsabilidades, restricciones y DoD de agents/skills/playbooks **sin cambio de significado** más allá de citas de versión y claridad de navegación.
- Constitución del método sigue en **sdaf-core**; este pack sigue siendo overlay.

## [0.1.0] — 2026-08-25

### Added

- Primera versión pública del pack: agents de extensión, skills, playbooks, `ADOPT.md`, `examples/`.
