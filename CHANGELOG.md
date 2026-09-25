# Changelog — sdaf-stack-dotnet

Formato basado en [Keep a Changelog](https://keepachangelog.com/). El semver del pack vive en [`pack.yaml`](pack.yaml). Las entradas publicadas no se reescriben; desde 0.3.0 las fechas nuevas llevan hora y zona (sdaf-core H13 §9).

## [0.3.0] — 2026-09-25T09:01+02:00

Cierre de la auditoría del pack v0.2.0 frente a sdaf-core 0.4.0. Trazabilidad: [worklog](worklogs/INIT-auditoria-v0.2.0/Iteration-001.md).

### Changed

- Compatibilidad **`sdaf_core: ">=0.4.0 <0.5.0"`** (deja la línea 0.3.x). Pin del core `v0.4.0`, `sdaf.version: "0.4.0"` en `examples/`, README y ADOPT; contrato enlazado a `v0.4.0`.
- Semver del pack a **0.3.0** en `pack.yaml`, cabeceras, citas `skill@version` y `stack.pack`. Contratos, prompts, skills y playbooks: **sin cambio de norma**.
- Contratos de agentes y playbooks: sección **Historial** con filas tomadas de los tags publicados (fecha del tag cuando la cabecera publicada no cuadraba con su versión).
- ADRs del pack: `ADR-0001`/`ADR-0002` → `ADR-001`/`ADR-002` (ficheros `ADR-NNN-slug.md`), estado `Aceptado` con la aceptación publicada que consta (PR #4); no es una aceptación nueva. Plantilla con hora, decisores y aceptación.
- Sitio MkDocs: `docs_dir` pasa a la raíz del repo, como sdaf-core desde 2026-09-20. Se retira `mkdocs/src/` (symlinks); los enlaces relativos a `CHANGELOG.md`, `pack.yaml`, `LICENSE` y `.cursor/` funcionan en GitHub y en el sitio. Dependencias alineadas con sdaf-core `v0.4.0` (Material 9.7, mike 2.2, pymdown 12).
- ADOPT: lista de pasos reparada (el paso 3 se renderizaba dentro de un aviso), upgrade 0.2.0 → 0.3.0 y action `validate-sdaf` del core como validación opcional.
- `check-md-links.ps1`: anclas contra el slug de GitHub **y** el de MkDocs; `-StrictAnchors` y `-StrictOrphans`.
- CI: acciones fijadas por SHA, `permissions` mínimos (solo el deploy escribe), build de docs y `docs-links` en todo PR; `docs-links` en modo estricto y con markdownlint (MD040, MD042).

### Added

- `scripts/check-pack-metadata.py` y su autocomprobación `scripts/test-check-pack-metadata.py` (20 mutaciones): `pack.yaml` ↔ cabeceras ↔ historial ↔ citas ↔ `examples/` ↔ README ↔ CHANGELOG ↔ ADRs.
- `scripts/check-history-append-only.py`: filas de Historial y entradas del CHANGELOG solo crecen respecto a la rama base.
- Workflow `validate.yml`: los checks anteriores, `examples/` con la action `validate-sdaf` del core `v0.4.0` (I4 estricto) y worklogs con `validate-worklog.py` del core.
- Gobierno: [`CODEOWNERS`](CODEOWNERS), [`SECURITY.md`](SECURITY.md), [`CONTRIBUTING.md`](CONTRIBUTING.md), `.editorconfig`, `.markdownlint.json`, `.github/dependabot.yml`; plantilla de PR con clase del cambio, historial y worklog.
- Primer worklog del pack (`worklogs/INIT-auditoria-v0.2.0/`).

### Notas

- Consumidores en **sdaf-core 0.3.x** se quedan en pack **0.2.0**.
- **Tag `v0.1.1`:** apunta a `c6c14d4` (2026-09-13) y no contiene lo que la entrada `[0.1.1]` de abajo describe (alineación a 0.1.1, UX GFM, checker de enlaces, CI), que entró en `main` el 2026-09-17 y se publicó por primera vez en `v0.2.0`. No se mueve el tag ni se reescribe la entrada (H08 §7 del core); las filas «0.1.1 · 2026-09-17» de skills y prompts describen ese estado de `main`.
- Queda pendiente, fuera de este repo: actualizar en sdaf-core las citas `sdaf-stack-dotnet@0.1.1` (contrato de pack, schema y `examples/` 04, 05, 07 y 08) cuando se publique `v0.3.0`.

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
