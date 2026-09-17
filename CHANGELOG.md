# Changelog — sdaf-stack-dotnet

Formato basado en [Keep a Changelog](https://keepachangelog.com/). El semver del pack vive en [`pack.yaml`](pack.yaml).

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
