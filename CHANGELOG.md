# Changelog — sdaf-stack-dotnet

Formato basado en [Keep a Changelog](https://keepachangelog.com/). El semver del pack vive en [`pack.yaml`](pack.yaml).

## [0.2.0] — 2026-09-19

### Changed

- Compatibilidad **`sdaf_core: ">=0.3.0 <0.4.0"`** (deja de declarar soporte de la línea 0.2.x).
- Semver del pack a **0.2.0** (`pack.yaml`, pin `v0.2.0`, `examples/`, citas `skill@version`, metadatos Pack/Versión).
- Escenarios: `sdaf.version: "0.3.0"`; alineados a los ejemplos 04/07 de sdaf-core v0.3.3.
- Contrato enlazado a [`contrato-pack-stack.md` @ v0.3.3](https://github.com/Cyberdine-Systems-Corporation/sdaf-core/blob/v0.3.3/docs/contrato-pack-stack.md).
- ADOPT: pin core `v0.3.3`, nota H06 (encargo git/remoto del turno), upgrade 0.2→0.3.

### Notas

- Consumidores en **sdaf-core 0.2.x** deben quedarse en pack **0.1.1** o subir primero el core a 0.3.x.
- Parte III del método (H09–H12) y skills `testing-review-pr` / `security-review` / `devops-ci-gate` viven en el core; este pack no las redefine.
- El merge de docs MkDocs (PR #7) ya está en `main` con el mismo árbol; no cambia el significado normativo del overlay.

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
