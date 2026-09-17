<!-- --8<-- [start:cuerpo] -->
# Domain+Application Agent

| Campo | Valor |
|--------|--------|
| Rol | Contrato de agente de extensión (fusión) |
| Versión | 0.1.1 |
| Estado | Approved |
| Fecha | 2026-09-13 |
| Modo | active (fusión; cuando el consumidor lo declare) |
| Prompt base | `prompts/agents/domain-application-agent.md` |
| Pack | sdaf-stack-dotnet@0.1.1 |

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

Implementar en .NET el slice de dominio + aplicación (fusión MVP) según specs Approved, sin separar Domain y Application salvo ADR del consumidor.

## Responsabilidades

- Modelar e implementar el vertical slice (comandos/consultas, invariantes).
- Seguir playbooks `coding-standards-csharp` y `vertical-slice-cqrs`.
- Invocar `csharp-adr006-slice` para el flujo de slice de API/aplicación.
- No poseer UI: handoff a Frontend cuando el PBI lo requiera.

## Entradas

Worklog; specs domain/application/acceptance Approved; ADRs; skills del pack.

## Salidas

Código de dominio/aplicación bajo `stack.src_path`; tests derivados; worklog.

## Restricciones

> [!WARNING]
> ⛔ Gate 0 obligatorio; no aprobar normas.

- Miembros `domain` y `application` no deben estar en `agents.active` a la vez que esta fusión.
- Sin secretos; castellano en artefactos de ingeniería.

## Checklist

- [ ] Gate 0
- [ ] Specs In citadas
- [ ] `csharp-adr006-slice@version` si aplica
- [ ] Handoff Frontend o Testing+Review

## KPIs

Un PBI → un slice coherente; acceptance mapeable.

## Definition of Done

✅ Slice In implementado o bloqueado con gap explícito; worklog cerrado hacia el siguiente agente.

<!-- --8<-- [end:cuerpo] -->

## Prompt base

[`prompts/agents/domain-application-agent.md`](../prompts/agents/domain-application-agent.md)

## Contexto autorizado

Índice. No sustituye al prompt base. No concatenar en un mega-prompt.

| Capa | Artefacto | Resumen (1 línea) | Obligatorio |
|------|-----------|-------------------|-------------|
| Rol | `prompts/agents/domain-application-agent.md` | Slice dominio+aplicación .NET | sí |
| Flujo | `skills/csharp-adr006-slice` | Vertical slice API/aplicación | según PBI |
| Flujo | `skills/sdaf-gate0` (sdaf-core) | Gate 0 antes de código | sí |
| Flujo | `skills/sdaf-worklog-handoff` (sdaf-core) | Cierre ATF / handoff | sí |
| IDE | `.cursor/rules/coding-standards-csharp.mdc` | Estándares C# del pack | si Cursor |
| IDE | `.cursor/rules/idioma-castellano.mdc` (consumidor/core) | Castellano en artefactos | si Cursor |

## Relacionado

| Destino | Por qué |
|---------|---------|
| [../prompts/agents/domain-application-agent.md](../prompts/agents/domain-application-agent.md) | Prompt de sistema |
| [../skills/csharp-adr006-slice/SKILL.md](../skills/csharp-adr006-slice/SKILL.md) | Skill del slice |
| [../playbooks/vertical-slice-cqrs.md](../playbooks/vertical-slice-cqrs.md) | Norma del slice |
| [../playbooks/coding-standards-csharp.md](../playbooks/coding-standards-csharp.md) | Estándares C# |
| [../README.md](../README.md) | Hub del pack |
