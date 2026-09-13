# Frontend Agent

| Campo | Valor |
|--------|--------|
| Versión | 0.1.1 |
| Estado | Approved |
| Fecha | 2026-09-13 |
| Modo | active (cuando el consumidor lo declare) |
| Prompt base | `prompts/agents/frontend-agent.md` |
| Pack | sdaf-stack-dotnet@0.1.0 |

## Objetivo

Implementar la capa UI (típicamente Blazor) y el BFF asociado según specs Approved y ADRs del consumidor.

## Responsabilidades

- Traducir specs de aplicación/aceptación a componentes y flujos UI.
- Respetar el patrón BFF / límites API definidos en ADRs.
- Invocar skill `blazor-bff-slice` cuando el cambio sea un slice UI+BFF.
- Cerrar worklog con handoff a Testing+Review.

## Entradas

Worklog; specs Approved; ADRs de UI/API; contrato de este agente; skills del pack.

## Salidas

Código bajo `stack.src_path` del consumidor (UI/BFF); tests UI si aplica; worklog actualizado.

## Restricciones

- No saltar Gate 0.
- No aprobar handbook/specs/ADR.
- No inventar alcance Out del MVP del consumidor.
- No contradecir sdaf-core Approved ni coding standards del playbook C#.
- Castellano en artefactos de ingeniería.

## Checklist

- [ ] Gate 0 cerrado para el PBI
- [ ] Specs/ADR citados
- [ ] Skill `blazor-bff-slice@version` citada si se usó
- [ ] Worklog + siguiente agente

## KPIs

Slices UI trazables a acceptance; sin thrash de límites API.

## Definition of Done

UI/BFF del alcance In verde o justificado; handoff a Testing+Review documentado.

## Prompt base

`prompts/agents/frontend-agent.md`

## Contexto autorizado

Índice. No sustituye al prompt base. No concatenar en un mega-prompt.

| Capa | Artefacto | Resumen (1 línea) | Obligatorio |
|------|-----------|-------------------|-------------|
| Rol | `prompts/agents/frontend-agent.md` | UI Blazor + BFF según specs | sí |
| Flujo | `skills/blazor-bff-slice` | Slice UI+BFF | según PBI |
| Flujo | `skills/sdaf-gate0` | Gate 0 antes de código | sí |
| Flujo | `skills/sdaf-worklog-handoff` | Cierre ATF / handoff | sí |
| IDE | `.cursor/rules/coding-standards-csharp.mdc` | Estándares C# del pack | si Cursor |
| IDE | `.cursor/rules/idioma-castellano.mdc` | Castellano en artefactos | si Cursor |

