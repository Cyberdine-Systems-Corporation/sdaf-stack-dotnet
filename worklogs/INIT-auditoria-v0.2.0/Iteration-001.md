---
pbi: INIT-auditoria-v0.2.0
iteracion: Iteration-001
fecha: 2026-09-24
inicio: 2026-09-24T20:21:29+02:00
fin: 2026-09-25T09:17:25+02:00
agente: humano + asistente IA (Claude Code)
modelo: "claude-sonnet-5 (auditoría e informe, 2026-09-24); claude-opus-5-5 (ejecución del plan, 2026-09-25)"
version_prompt: N/D
prompt_base: ninguno (encargo ad hoc en chat; sin prompt versionado de prompts/)
prompts_adicionales: ninguno
skills: ninguna
reglas_ide: ninguna (sesión fuera de Cursor)
ad_hoc: "Encargos del humano en chat: «auditoría del repositorio como hemos hecho con sdaf-core» (alcance elegido: solo informe; compat elegida: core 0.4.x → pack 0.3.0) y, en un turno posterior, «Ejecuta el plan». El plan de 16 hallazgos (P01–P16) vive fuera del repo; su resumen está en este worklog."
contexto: "Auditoría de sdaf-stack-dotnet v0.2.0 frente a la línea 0.4.0 de sdaf-core y ejecución del plan resultante: pack 0.3.0 compatible con core 0.4.x."
especificaciones_utilizadas: "sdaf-core v0.4.0: docs/contrato-pack-stack.md; docs/adopcion-y-upgrade.md §0.4.0; handbook/06 §7; handbook/08 §5–§7; handbook/10 §3.1; handbook/13 §5–§9; templates/worklog.md; worklog.schema.json; .github/actions/validate-sdaf; worklogs/INIT-auditoria-v0.3.3/Iteration-001.md (precedente de formato)"
archivos_leidos: "Todo el árbol versionado del pack (29 .md, pack.yaml, examples/, mkdocs/, .github/, scripts/, .cursor/); tags v0.1.0, v0.1.1 y v0.2.0 (cabeceras y contenido); en sdaf-core: CHANGELOG, handbook/CHANGELOG, H06, H08, H13, validate.yml, docs-deploy.yml, mkdocs.yml, scripts/check-local-links.py, validate-config.py, validate-worklog.py, CODEOWNERS, SECURITY.md, .editorconfig, .markdownlint.json, dependabot.yml, requirements-docs.txt"
archivos_modificados: "Raíz: pack.yaml, README.md, ADOPT.md, CHANGELOG.md, CONTRIBUTING.md (nuevo), SECURITY.md (nuevo), CODEOWNERS (nuevo), .editorconfig (nuevo), .markdownlint.json (nuevo), .gitignore, requirements-docs.txt. Artefactos: agents/*.md, prompts/agents/*.md, skills/README.md y skills/*/SKILL.md, playbooks/*.md, .cursor/rules/coding-standards-csharp.mdc, examples/*.yaml. Docs: docs/adoption/escenarios.md, docs/architecture/ (index, relacion-componentes, adr/index, plantilla-adr, ADR-001 y ADR-002 renombrados desde 0001/0002), docs/checklist-pagina-docs.md, docs/navegacion-docs.md, docs/uso-local.md. Sitio: mkdocs/mkdocs.yml, mkdocs/README.md, mkdocs/src/ retirado. CI: .github/workflows/validate.yml (nuevo), docs.yml, docs-links.yml, dependabot.yml (nuevo), pull_request_template.md. Tooling: scripts/check-pack-metadata.py, scripts/test-check-pack-metadata.py, scripts/check-history-append-only.py (nuevos), scripts/check-md-links.ps1. Este worklog."
origen_cambios: N/A
resultado: "Pack 0.3.0: compat sdaf-core >=0.4.0 <0.5.0, pin v0.4.0 y sdaf.version 0.4.0 en README, ADOPT y examples. Historial en contratos y playbooks (filas de los tags) y fila 0.3.0 con hora y zona en los 11 artefactos versionados, sin cambio de norma. ADRs como ADR-001/002 con la aceptación publicada que consta. Sitio con docs_dir en la raíz (modelo actual del core) sin symlinks. Checkers nuevos (metadatos del pack con 20 mutaciones, historial que solo crece) y checker de enlaces con slugs de GitHub y MkDocs en modo estricto. CI por SHA con permisos mínimos; examples validados con la action validate-sdaf del core y worklogs con su validador. Gobierno: CODEOWNERS, SECURITY, CONTRIBUTING, editorconfig, markdownlint, dependabot, plantilla de PR."
tiempo: "N/D: la app se cerró dos veces y la sesión quedó parada entre turnos; el reloj inicio→fin (≈13 h) no mide trabajo y la herramienta no expone el tiempo activo"
coste:
  modalidad: suscripcion
  importe: null
  moneda: null
  tokens: 280679
  fuente: "get_usage de Claude Code el 2026-09-25 hacia las 09:15 (+02:00): tokens de contexto de la sesión, no el total procesado. Plan Pro sin importe por uso; la sesión consumió cuota del plan (18 % de la ventana de 5 h en esa lectura), no atribuible solo a ella."
observaciones: "Hallazgo nuevo durante la ejecución (P17): el tag v0.1.1 (c6c14d4, 2026-09-13) no contiene lo que la entrada [0.1.1] del CHANGELOG describe; entró en main el 2026-09-17 y se publicó con v0.2.0. Se declara en el CHANGELOG 0.3.0; no se mueve el tag ni se reescribe la entrada. P14 (vocabulario visual) se descartó: no hay emoji en headings. Desvío del criterio de sdaf-core H13 §8 («fila inicial que repite la cabecera»): las filas nuevas de Historial de contratos y playbooks salen de los tags publicados, porque la cabecera de los contratos (0.2.0 · 2026-09-13) mezclaba versión y fecha de tags distintos. docs-links.yml se conserva en vez de fusionarlo en validate.yml porque la entrada publicada [0.1.1] lo enlaza. La aceptación de los ADR no es nueva: solo cambia el vocabulario del estado; confirmarlo corresponde a la identidad de CODEOWNERS en la revisión. SECURITY.md no fija tabla de soporte por versión (decisión del mantenedor). Pendiente fuera del repo (P16): actualizar en sdaf-core las citas sdaf-stack-dotnet@0.1.1 tras publicar v0.3.0. Sin commit, PR ni tag en esta iteración: cada uno exige orden humana expresa (H06 §7)."
pruebas_ejecutadas: "Locales, exit 0: check-pack-metadata.py; test-check-pack-metadata.py (20/20 mutaciones detectadas); check-history-append-only.py --base origin/main (y dos mutaciones de prueba detectadas: fila publicada reescrita, sección del CHANGELOG reescrita; base irresoluble → exit 2); check-md-links.ps1 -StrictAnchors -StrictOrphans (más un árbol de prueba con headings «—», emoji, duplicados y tildes); validate-config.py de sdaf-core v0.4.0 --strict-i4 --consumer-root . sobre examples/*.yaml; validate-worklog.py de sdaf-core v0.4.0 sobre este worklog; mkdocs build --strict (mkdocs 1.6.1, Material 9.7.7, pymdown 12.1); MD040 y MD042 comprobadas con script local (sin Node). No ejecutado en local: markdownlint-cli2 y los workflows de GitHub Actions."
estado: hecho
siguiente_agente: humano (revisión del diff, commit, PR, merge y tag v0.3.0)
commit: null
pr: null
rama: feat/pack-0.3.0
sha: null
resumen_acumulado: "ad hoc (chat) — auditoría del pack v0.2.0 → pack 0.3.0 (core 0.4.x); commit/PR/SHA en la descripción del PR; rama feat/pack-0.3.0"
---

# INIT-auditoria-v0.2.0 / Iteration-001

## Hallazgos y resolución

| Id | Hallazgo | Resolución |
|----|----------|------------|
| P01 | Compat `sdaf_core ">=0.3.0 <0.4.0"` con core vigente 0.4.0 | Pack 0.3.0, `>=0.4.0 <0.5.0`, pin `v0.4.0` |
| P02 | Coherencia de versiones solo manual | `check-pack-metadata.py` + autocomprobación |
| P03 | `examples/` sin validar | Action `validate-sdaf` del core en CI (I4 estricto) |
| P04 | Contratos y playbooks sin Historial; fechas de cabecera incoherentes; sin worklog | Historial desde tags; fila 0.3.0 con hora; este worklog |
| P05 | Sin CODEOWNERS, SECURITY, CONTRIBUTING, editorconfig, markdownlint, dependabot | Añadidos |
| P06 | Acciones por tag, `contents: write` global, dependencias MkDocs viejas | SHA, permisos por job, versiones del core |
| P07 | «0.1.x»/«0.2.x» obsoletos; ADRs `0001`/`Approved` | Textos vivos corregidos; `ADR-001`/`Aceptado`; cuerpo de ADR intacto |
| P08 | Checker de enlaces laxo y con slug propio | Slugs GitHub + MkDocs; `-StrictAnchors`, `-StrictOrphans` |
| P09 | PR que solo toca README no construía el sitio | `docs` y `docs-links` en todo PR |
| P10 | Paso 3 de ADOPT dentro de un aviso | Lista con bloques sangrados |
| P11 | Stubs de los ejemplos sin explicar | Comentarios y sección en escenarios |
| P12 | Enlaces a `blob/main` | `docs_dir` en la raíz; relativos salvo tooling excluido |
| P13 | Entidades HTML en texto | Código en línea; plantilla nueva |
| P14 | Vocabulario visual | Descartado: la regla se cumple |
| P15 | Regla Cursor y «activo» sin remitir a config | Referencias añadidas |
| P16 | sdaf-core cita el pack `@0.1.1` | Pendiente en sdaf-core tras publicar `v0.3.0` |
| P17 | Tag `v0.1.1` no contiene lo que su entrada describe | Declarado en el CHANGELOG 0.3.0 |

## Línea de decisión

- Compat 0.4.x y pack 0.3.0: elección humana en el encargo.
- Filas de Historial desde los tags (dato verificable) en lugar de repetir cabeceras incoherentes; se aparta de H13 §8 del core por ese motivo.
- Filas y entradas publicadas no se tocan (H08 §7); las discrepancias se declaran en la entrada nueva.
- `docs_dir: ..` como sdaf-core desde 2026-09-20: elimina la dependencia de symlinks en Windows y el motivo de los enlaces absolutos.
- Este worklog existe porque el cambio toca contratos, skills, playbooks y ADRs (H08 §5 del core).

## Origen de cambios

| Archivo | Origen | Notas |
|---------|--------|-------|
| N/A (esta iteración no toca código de producto) | | El pack no contiene producto. Norma y tooling: redacción IA; alcance, compat y aceptación humanas. |

`commit`, `pr` y `sha` quedan en `null`: el worklog entra en el mismo commit que documenta y no puede contener su propio SHA. Se enlazan desde la descripción del PR.
