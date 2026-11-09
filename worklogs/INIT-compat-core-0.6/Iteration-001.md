---
pbi: INIT-compat-core-0.6
iteracion: Iteration-001
fecha: 2026-11-09
inicio: 2026-11-09T19:35:00+01:00
fin: 2026-11-09T19:44:25+01:00
agente: asistente IA (Claude Code), por encargo del humano
modelo: "claude-sonnet-5-5"
version_prompt: N/D
prompt_base: ninguno (encargo ad hoc; sin prompt versionado de prompts/)
prompts_adicionales: ninguno
skills: ninguna
reglas_ide: ninguna (sesión fuera de Cursor)
ad_hoc: "Encargo del humano (fase B, cambio local): pack 0.4.0 compatible con sdaf-core 0.6.x, con sdaf-pack.yaml. Decisiones del humano, una a una: versión 0.4.0; rango core '>=0.6.0 <0.7.0'; pack.yaml y sdaf-pack.yaml conviven con un check de coherencia cruzada; provides con extensiones, skills y prompts (id del agente); validación a mano ahora y paso de CI cuando exista el tag v0.6.0 del core; examples/ con stack.packs y sdaf.version '0.6.0' y la action validate-sdaf fijada a un SHA de main del core hasta ese tag."
contexto: "Pack sdaf-stack-dotnet 0.3.0 (core 0.4.x) frente a la línea 0.6 de sdaf-core, que lee un manifiesto sdaf-pack.yaml y declara los packs en stack.packs."
especificaciones_utilizadas: "sdaf-core (main, 60e9e5b): docs/contrato-pack-stack.md (Manifiesto, Relación con stack.packs, Ruta normada de los packs); sdaf-pack.schema.json; templates/sdaf-pack.yaml; scripts/validate-pack.py y validate-config.py; commit f15f96b de este pack como modelo de un cambio de compatibilidad y release; CONTRIBUTING.md del pack (clase del cambio, historial y worklog)"
archivos_leidos: "Todo el árbol versionado del pack que lleva versión o cita (contratos, prompts, skills, playbooks, README, ADOPT, CONTRIBUTING, CHANGELOG, pack.yaml, examples/, docs/, ADRs, workflows, scripts/); en sdaf-core: docs/contrato-pack-stack.md, sdaf-pack.schema.json, templates/sdaf-pack.yaml, validate-config.py, validate-pack.py, materialize.py, action validate-sdaf, templates/worklog.md y worklog.schema.json en v0.4.2"
archivos_modificados: "Nuevo: sdaf-pack.yaml, este worklog. Raíz: pack.yaml, README.md, ADOPT.md, CHANGELOG.md, CONTRIBUTING.md. Artefactos versionados: agents/*.md, prompts/agents/*.md, skills/*/SKILL.md, playbooks/*.md (cabecera Pack/Versión/Fecha, citas skill@version y fila 0.4.0 del Historial). Índices y docs: agents/README.md, playbooks/README.md, skills/README.md, docs/adoption/escenarios.md, docs/navegacion-docs.md, docs/architecture/index.md, docs/architecture/adr/ADR-001 y ADR-002 (Vigente en), docs/uso-local.md. Escenarios: examples/01-pack-only.yaml, examples/02-pack-frontend.yaml. CI: .github/workflows/validate.yml (solo el pin de validate-sdaf). Tooling: scripts/check-pack-metadata.py, scripts/test-check-pack-metadata.py."
origen_cambios: N/A
resultado: "Pack 0.4.0: sdaf_core '>=0.6.0 <0.7.0' en pack.yaml y core en sdaf-pack.yaml (id, version, provides.extension_ids, skills y prompts); fila 0.4.0 con hora y zona en los 11 artefactos versionados, sin cambio de norma; examples/ con stack.packs y sdaf.version '0.6.0'; check-pack-metadata cruza sdaf-pack.yaml con pack.yaml y lee stack.packs (autocomprobación de 20 a 31 mutaciones, todas detectadas); validate-sdaf del CI fijada a un SHA de main del core."
tiempo: "N/D: la herramienta no expone el tiempo activo de la sesión"
coste: "N/D: la herramienta no expone tokens ni importe de esta sesión"
observaciones: "Fecha de la release: la entrada [0.4.0] del CHANGELOG y las filas de Historial llevan la hora de registro del cambio (como 0.3.0 en f15f96b); quien publique ajusta la fecha de la release si difiere. La entrada [Unreleased] se funde en [0.4.0]. Hallazgo de la validación a mano: con --pack-manifest sdaf-pack.yaml y --strict-i4, los dos examples/ fallan en I4 por el id 'ai' (en stubs): lo conoce el core como id de extensión y este pack no lo aporta (provides.extension_ids = domain-application, frontend, infrastructure). Sin manifiesto, que es como la action validate-sdaf del CI invoca el validador, pasan con un aviso. Decisión pendiente antes de añadir el paso de CI con manifiesto: quitar 'ai' de los stubs de los ejemplos o aceptar el aviso sin --strict-i4. Los enlaces al core apuntan a v0.6.0, tag que aún no existe. El validador de worklog del CI sigue en core v0.4.2."
pruebas_ejecutadas: "Locales, exit 0: test-check-pack-metadata.py primero en RED (9 mutaciones del manifiesto aceptadas por el checker anterior, y el árbol con stack.packs rechazado) y después 31/31 mutaciones detectadas más la variante del alias aceptada; check-pack-metadata.py; check-history-append-only.py --base origin/main; validate-pack.py de sdaf-core sobre sdaf-pack.yaml; validate-config.py de sdaf-core con --pack-manifest sobre examples/*.yaml (sin --strict-i4: exit 0 con avisos de I4; con --strict-i4: exit 1 por el id 'ai', ver observaciones); validate-config.py --strict-i4 sin manifiesto, como la action del CI: exit 0 con aviso de manifiesto ausente; validate-worklog.py de sdaf-core v0.4.2 sobre este worklog; mkdocs build --strict. No ejecutado en local: markdownlint-cli2 y los workflows de GitHub Actions."
estado: hecho
siguiente_agente: humano (revisión del diff, commit, push, PR y release del pack)
commit: null
pr: null
rama: compat/sdaf-core-0.6
sha: null
resumen_acumulado: "ad hoc (chat) — pack 0.4.0 compatible con sdaf-core 0.6.x con sdaf-pack.yaml; sin commit; rama compat/sdaf-core-0.6"
---

# INIT-compat-core-0.6 / Iteration-001

## Línea de decisión

- Versión 0.4.0 y rango `>=0.6.0 <0.7.0`: decisión del humano; cambio de compatibilidad = minor del pack (CONTRIBUTING, clase «Compat»). No se reetiqueta `v0.3.0`.
- `pack.yaml` y `sdaf-pack.yaml` conviven: el schema del core es cerrado (`additionalProperties: false`) y no admite `description`, `playbooks` ni `limits`, que siguen en `pack.yaml`. `check-pack-metadata.py` comprueba que coincidan.
- `provides.prompts` usa el id del agente (`frontend`, `domain-application`, `infrastructure`), el mismo que el nombre de fichero `prompts/agents/<id>-agent.md`.
- Los ejemplos pasan a `stack.packs`; el checker del pack sigue leyendo el alias `stack.pack`.
- Decisión del humano (2026-11-09): se quita `ai` de los `stubs` de `examples/01-pack-only.yaml` y `examples/02-pack-frontend.yaml`. El core lo trata como id de extensión que este pack no aporta, así que con el manifiesto y `--strict-i4` fallaba la comprobación I4; los ejemplos del core tampoco lo llevan.
- La action `validate-sdaf` queda fijada al SHA `60e9e5b` de `main` del core hasta que exista `v0.6.0`, porque el schema de `v0.5.3` no conoce `stack.packs`. El paso con `validate-pack.py` y `--pack-manifest` se añade con ese tag. `docs.yml` y los disparadores de release no se tocan.
- Este worklog existe porque el cambio toca contratos, prompts, skills y playbooks (alineación de versión, sin cambio de obligación).

## Origen de cambios

| Archivo | Origen | Notas |
|---------|--------|-------|
| N/A (esta iteración no toca código de producto) | | El pack no contiene producto. Redacción IA; alcance, versión y rango, humanos. |

`commit`, `pr` y `sha` quedan en `null`: el worklog entra en el mismo commit que documenta y no puede contener su propio SHA.
