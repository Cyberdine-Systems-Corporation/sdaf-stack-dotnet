<!-- --8<-- [start:cuerpo] -->
# Infrastructure Agent

| Campo | Valor |
|--------|--------|
| Rol | Contrato de agente de extensión (stub) |
| Versión | 0.3.0 |
| Estado | Approved |
| Fecha | 2026-09-25T09:01+02:00 |
| Modo | stub |
| Prompt base | `prompts/agents/infrastructure-agent.md` |
| Pack | sdaf-stack-dotnet@0.3.0 |

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
- [Historial](#historial)
- [Relacionado](#relacionado)

## Objetivo

Persistencia y adapters de infraestructura cuando el humano active este stub (no forma parte del handoff canónico; ver [ADR-002](../docs/architecture/adr/ADR-002-infrastructure-stub.md)).

## Responsabilidades

Activar solo bajo demanda humana explícita. Preparar contrato+prompt para desacople futuro.

## Entradas

Encargo explícito; worklog; ADRs de persistencia/adapters.

## Salidas

Adapters / infra según layout del consumidor.

## Restricciones

> [!WARNING]
> ⛔ Stub = no invocar por defecto. Gate 0 si toca producto. No aprobar normas.

## Checklist

- [ ] Encargo explícito
- [ ] Worklog

## KPIs

Uso justificado.

## Definition of Done

✅ Entrega puntual + handoff documentado.

<!-- --8<-- [end:cuerpo] -->

## Prompt base

[`prompts/agents/infrastructure-agent.md`](../prompts/agents/infrastructure-agent.md)

## Contexto autorizado

Índice. Stub: solo contrato + prompt base hasta activación humana explícita. No mega-prompt.

| Capa | Artefacto | Resumen (1 línea) | Obligatorio |
|------|-----------|-------------------|-------------|
| Rol | `prompts/agents/infrastructure-agent.md` | Persistencia/adapters bajo demanda | sí (si se activa) |
| Flujo | `skills/sdaf-gate0` (sdaf-core) | Gate 0 si toca producto | si implementación |
| Flujo | `skills/sdaf-worklog-handoff` (sdaf-core) | Cierre ATF / handoff | sí (si se activa) |
| IDE | `.cursor/rules/coding-standards-csharp.mdc` | Estándares C# del pack | si Cursor |
| IDE | `.cursor/rules/idioma-castellano.mdc` (consumidor/core) | Castellano en artefactos | si Cursor |

## Historial

| Versión | Fecha | Cambio |
|---------|--------|--------|
| 0.1.0 | 2026-08-25 | Primera versión del pack (tag `v0.1.0`) |
| 0.1.1 | 2026-09-13 | Publicado en tag `v0.1.1` |
| 0.2.0 | 2026-09-19 | Compat sdaf-core 0.3.x; pack@0.2.0 (tag `v0.2.0`; la cabecera publicada decía 2026-09-13) |
| 0.3.0 | 2026-09-25T09:01+02:00 | Compat sdaf-core 0.4.x; pack@0.3.0. Historial añadido desde los tags publicados. Sin cambio de norma. |

## Relacionado

| | Destino | Por qué |
|--|---------|---------|
| 📝 | [../prompts/agents/infrastructure-agent.md](../prompts/agents/infrastructure-agent.md) | Prompt de sistema |
| 📖 | [../playbooks/vertical-slice-cqrs.md](../playbooks/vertical-slice-cqrs.md) | Cuándo aparecen puertos/adapters |
| 🧭 | [../README.md](../README.md) | Hub del pack |
