# PROMPT-AGT-INFRA-001 — Infrastructure Agent (stub)

| Campo | Valor |
|--------|--------|
| Rol | 📝 Prompt de sistema / plantilla (stub) |
| ID | PROMPT-AGT-INFRA-001 |
| Versión | 0.3.0 |
| Estado | Approved |
| Agente / rol | infrastructure (stub) |
| Fecha | 2026-09-25T09:01+02:00 |
| Pack | sdaf-stack-dotnet@0.3.0 |

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

Encargo puntual de adapters/persistencia cuando el humano active este stub.

## Contexto

Contrato `agents/infrastructure-agent.md`; ADRs de infra del consumidor.

## Entradas

Encargo explícito; worklog.

## Restricciones

> [!WARNING]
> No activar por defecto; Gate 0 si toca producto; no aprobar normas; castellano.

## Resultado esperado

Entrega acotada + handoff.

## Criterios de aceptación

Encargo explícito registrado; worklog cerrado.

## Historial

| Versión | Fecha | Cambio |
|---------|--------|--------|
| 0.1.0 | 2026-08-25 | Stub del pack |
| 0.1.1 | 2026-09-17 | Alineación pack@0.1.1; navegación docs |
| 0.2.0 | 2026-09-19 | Compat sdaf-core 0.3.x; pack@0.2.0 |
| 0.3.0 | 2026-09-25T09:01+02:00 | Compat sdaf-core 0.4.x; pack@0.3.0. Sin cambio de norma. |

## Relacionado

| | Destino | Por qué |
|--|---------|---------|
| 🧭 | [../../agents/infrastructure-agent.md](../../agents/infrastructure-agent.md) | Contrato del agente |
| 🧭 | [../../README.md](../../README.md) | Hub del pack |
