## Resumen

<!-- 1–3 frases. Si tocas contratos, skills o playbooks Approved, declara si la obligación permanece. -->

## Clase del cambio

- [ ] **Redacción**: la obligación no cambia; historial «Sin cambio de norma», bump patch del artefacto si aplica.
- [ ] **Significado**: cambia una obligación de un contrato, skill o playbook Approved; bump y entrada en `CHANGELOG.md`.
- [ ] **Compat / release**: cambia `version` o `sdaf_core` en `pack.yaml`; entrada en `CHANGELOG.md` y upgrade en `ADOPT.md`.

## Plan de prueba

- [ ] CI verde: `validate` (metadatos del pack, historial, examples, worklogs), `Docs links` (enlaces estrictos, markdownlint) y `docs` (build estricto).
- [ ] Si el PR toca markdown: checklist [`docs/checklist-pagina-docs.md`](../docs/checklist-pagina-docs.md).
- [ ] Si cambia una versión: fila nueva en **Historial** con fecha ISO 8601 con hora y zona; filas publicadas intactas.
- [ ] Si el cambio es material (contrato, skill, playbook, prompt o ADR): worklog bajo `worklogs/` (H08 §5 del core).
