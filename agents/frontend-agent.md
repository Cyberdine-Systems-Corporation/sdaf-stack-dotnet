<!-- --8<-- [start:cuerpo] -->
# Frontend Agent

| Campo | Valor |
|--------|--------|
| Rol | Contrato de agente de extensión |
| Versión | 0.2.0 |
| Estado | Approved |
| Fecha | 2026-09-13 |
| Modo | active (cuando el consumidor lo declare) |
| Prompt base | `prompts/agents/frontend-agent.md` |
| Pack | sdaf-stack-dotnet@0.2.0 |

## En esta página

- [Objetivo](#objetivo)
- [Responsabilidades](#responsabilidades)
- [Entradas](#entradas)
- [Salidas](#salidas)
- [Restricciones](#restricciones)
- [Checklist](#checklist)
- [KPIs](#kpis)
- [Definition of Done](#definition-of-done)
- [Prompt base](#prompt-base)
- [Contexto autorizado](#contexto-autorizado)
- [Relacionado](#relacionado)

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

> [!WARNING]
> ⛔ No saltar Gate 0. No aprobar handbook/specs/ADR.

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

✅ UI/BFF del alcance In verde o justificado; handoff a Testing+Review documentado.

<!-- --8<-- [end:cuerpo] -->

## Prompt base

[`prompts/agents/frontend-agent.md`](../prompts/agents/frontend-agent.md)

## Contexto autorizado

Índice. No sustituye al prompt base. No concatenar en un mega-prompt.

| Capa | Artefacto | Resumen (1 línea) | Obligatorio |
|------|-----------|-------------------|-------------|
| Rol | `prompts/agents/frontend-agent.md` | UI Blazor + BFF según specs | sí |
| Flujo | `skills/blazor-bff-slice` | Slice UI+BFF | según PBI |
| Flujo | `skills/sdaf-gate0` (sdaf-core) | Gate 0 antes de código | sí |
| Flujo | `skills/sdaf-worklog-handoff` (sdaf-core) | Cierre ATF / handoff | sí |
| IDE | `.cursor/rules/coding-standards-csharp.mdc` | Estándares C# del pack | si Cursor |
| IDE | `.cursor/rules/idioma-castellano.mdc` (consumidor/core) | Castellano en artefactos | si Cursor |

## Relacionado

| | Destino | Por qué |
|--|---------|---------|
| 📝 | [../prompts/agents/frontend-agent.md](../prompts/agents/frontend-agent.md) | Prompt de sistema |
| 🛠️ | [../skills/blazor-bff-slice/SKILL.md](../skills/blazor-bff-slice/SKILL.md) | Skill UI+BFF |
| 📖 | [../playbooks/coding-standards-csharp.md](../playbooks/coding-standards-csharp.md) | Estándares C# |
| 🧭 | [../README.md](../README.md) | Hub del pack |
