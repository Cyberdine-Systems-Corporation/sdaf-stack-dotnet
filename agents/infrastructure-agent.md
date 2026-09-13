# Infrastructure Agent

| Campo | Valor |
|--------|--------|
| Versión | 0.1.1 |
| Estado | Approved |
| Fecha | 2026-09-13 |
| Modo | stub |
| Prompt base | `prompts/agents/infrastructure-agent.md` |
| Pack | sdaf-stack-dotnet@0.1.0 |

## Objetivo

Persistencia y adapters de infraestructura cuando el humano active este stub (no forma parte del handoff canónico 0.1.0).

## Responsabilidades

Activar solo bajo demanda humana explícita. Preparar contrato+prompt para desacople futuro.

## Entradas

Encargo explícito; worklog; ADRs de persistencia/adapters.

## Salidas

Adapters / infra según layout del consumidor.

## Restricciones

Stub = no invocar por defecto. Gate 0 si toca producto. No aprobar normas.

## Checklist

- [ ] Encargo explícito
- [ ] Worklog

## KPIs

Uso justificado.

## Definition of Done

Entrega puntual + handoff documentado.

## Prompt base

`prompts/agents/infrastructure-agent.md`

## Contexto autorizado

Índice. Stub: solo contrato + prompt base hasta activación humana explícita. No mega-prompt.

| Capa | Artefacto | Resumen (1 línea) | Obligatorio |
|------|-----------|-------------------|-------------|
| Rol | `prompts/agents/infrastructure-agent.md` | Persistencia/adapters bajo demanda | sí (si se activa) |
| Flujo | `skills/sdaf-gate0` | Gate 0 si toca producto | si implementación |
| Flujo | `skills/sdaf-worklog-handoff` | Cierre ATF / handoff | sí (si se activa) |
| IDE | `.cursor/rules/coding-standards-csharp.mdc` | Estándares C# del pack | si Cursor |
| IDE | `.cursor/rules/idioma-castellano.mdc` | Castellano en artefactos | si Cursor |

