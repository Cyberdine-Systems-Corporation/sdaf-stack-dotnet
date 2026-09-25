# Checklist de página (docs / contratos / skills / playbooks)

Usar en el DoD de un PR que toque markdown del pack. Marcar lo aplicable.

1. **Título** dice qué es la página en una línea.
2. **Rol** explícito: HOWTO, contrato, playbook, skill, plantilla, ADR del pack o índice.
3. **Puerta de entrada:** un lector nuevo llega en ≤3 clics desde el [README](../README.md) (Inicio del sitio MkDocs).
4. **En esta página** (TOC) si hay más de tres headings `##`.
5. **Relacionado** al cierre (tabla destino / por qué; icono del set cerrado cuando aporta), sin bucles vacíos.
6. **Enlaces** relativos a archivos que existen, también hacia `CHANGELOG.md`, `pack.yaml` o `.cursor/` (el sitio usa la raíz del repo como `docs_dir`). Evitar `blob/main/…` salvo para tooling excluido del sitio (`.github/`, `mkdocs/`). CI: `scripts/check-md-links.ps1 -StrictAnchors -StrictOrphans`.
7. **Anclas** coinciden con el slug del heading en GitHub **y** en MkDocs (`slugify_unicode`): minúsculas, tildes conservadas. Evita en headings signos que dejen dos espacios seguidos al borrarse (` — `, ` / `, ` + `): GitHub genera `--`, MkDocs `-`, y el ancla solo vale en uno.
8. **Un diagrama** (Mermaid) si hay un flujo de ≥3 pasos; árboles de carpetas pueden seguir en ` ```text `. Color: rojo STOP, verde Approved/listo, gris stub, azul constitución/core.
9. **Tablas** para catálogos, gates y comparaciones; no párrafos-lista de 10 ítems.
10. **Fences** con lenguaje (`text`, `yaml`, `markdown`, `mermaid`, `csharp`, …).
11. **Voz activa**, párrafos cortos, castellano directo.
12. **Jerga del método** (Gate 0, ATF, Approved, pack, overlay) con glosa de una línea la primera vez en páginas HOWTO.
13. **Sin pegar** handbook de sdaf-core ni specs de producto (economía de tokens).
14. **Versión** del pack coherente con [CHANGELOG.md](../CHANGELOG.md) / `pack.yaml` cuando se cite un tag.
15. **Significado normativo** de contratos y playbooks Approved intacto: solo claridad, TOC, Relacionado, diagrama o alerta GFM.
16. **Vocabulario visual cerrado** ([navegación](navegacion-docs.md#vocabulario-visual)): icono o alerta GFM cuando hay STOP, Draft/Approved o cambio de rol (constitución vs HOWTO vs overlay). Prohibido emoji libre. Cero emoji en headings de páginas normativas.
17. **No sustituir** la constitución de sdaf-core ni redefinir agentes núcleo (`specification`, `architecture`, `testing-review`).
18. **Versión e historial** (contratos, prompts, skills, playbooks): cambio de versión = fila nueva en **Historial**; las filas publicadas no se tocan. Fecha nueva en ISO 8601 con hora y zona (`AAAA-MM-DDThh:mm±hh:mm`, H13 §9 del core); la `Fecha` de cabecera es la de la fila más reciente. CI: `scripts/check-pack-metadata.py` y `scripts/check-history-append-only.py`.
19. **Worklog** bajo `worklogs/` si el cambio es material (contrato, playbook, skill o ADR; H08 §5 del core).

## Relacionado

| | Destino | Por qué |
|--|---------|---------|
| 🧭 | [navegacion-docs.md](navegacion-docs.md) | Tres puertas, clics y vocabulario visual |
| 🛠️ | [uso-local.md](uso-local.md) | Build local y publicación mike |
| 📦 | [README.md](../README.md) | Hub del pack |
