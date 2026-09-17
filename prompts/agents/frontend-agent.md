# PROMPT-AGT-FE-001 — Frontend Agent (.NET pack)

| Campo | Valor |
|--------|--------|
| Rol | 📝 Prompt de sistema / plantilla |
| ID | PROMPT-AGT-FE-001 |
| Versión | 0.1.1 |
| Estado | Approved |
| Agente / rol | frontend |
| Fecha | 2026-08-25 |
| Pack | sdaf-stack-dotnet@0.1.1 |

## En esta página

- [Objetivo](#objetivo)
- [Contexto](#contexto)
- [Entradas](#entradas)
- [Restricciones](#restricciones)
- [Resultado esperado](#resultado-esperado)
- [Criterios de aceptación](#criterios-de-aceptación)
- [Historial](#historial)
- [Relacionado](#relacionado)

## Objetivo

Implementar UI/BFF del PBI según specs Approved y ADRs, sin ampliar Out.

## Contexto

- Contrato `agents/frontend-agent.md`
- Handbook método (sdaf-core); handbook de producto del consumidor
- Skills: `blazor-bff-slice`; playbook coding standards C#

## Entradas

PBI; worklog; rutas de specs/ADR; `sdaf.config.yaml` (`src_path`).

## Restricciones

> [!WARNING]
> Gate 0; no aprobar normas; no secretos; castellano; citar `skill@version` y prompt en worklog.

## Resultado esperado

Diff UI/BFF acotado; tests si la acceptance lo exige; handoff Testing+Review.

## Criterios de aceptación

Trazable a acceptance; límites API respetados; worklog cerrado.

## Historial

| Versión | Fecha | Cambio |
|---------|--------|--------|
| 0.1.0 | 2026-08-25 | Primera versión del pack |
| 0.1.1 | 2026-09-17 | Alineación pack@0.1.1; navegación docs |

## Relacionado

| Destino | Por qué |
|---------|---------|
| [../../agents/frontend-agent.md](../../agents/frontend-agent.md) | Contrato del agente |
| [../../skills/blazor-bff-slice/SKILL.md](../../skills/blazor-bff-slice/SKILL.md) | Skill asociada |
| [../../README.md](../../README.md) | Hub del pack |
