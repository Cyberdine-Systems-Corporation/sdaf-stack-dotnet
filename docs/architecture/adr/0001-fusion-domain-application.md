# ADR-0001 · Fusión `domain-application` en 0.1.x

| Campo | Valor |
|--------|--------|
| Estado | Approved |
| Fecha | 2026-09-13 |
| Pack | `sdaf-stack-dotnet@0.1.1` |

## Contexto

Un pack de stack para MVPs en .NET no necesita, desde el día uno, separar los agentes `domain` y `application` del núcleo SDAF: montar ambas capas vacías "para el futuro" contradice el principio de vertical slice (ver [`playbooks/vertical-slice-cqrs.md`](../../playbooks/vertical-slice-cqrs.md)).

## Decisión

Se define un único agente de extensión **`domain-application`** (fusión) que implementa dominio + aplicación como un solo slice, invocando la skill [`csharp-adr006-slice`](../../skills/csharp-adr006-slice.md). La separación de capas solo ocurre si un ADR del **consumidor** la exige explícitamente.

## Alternativas consideradas

- Dos agentes independientes (`domain`, `application`) activos desde 0.1.0 — descartada: añade ceremonia sin PBI que la justifique en un MVP.
- Sin agente propio, delegando todo a `sdaf-core` — descartada: el core no conoce las convenciones C#/.NET del stack (naming, nullable, async).

## Consecuencias

- Positivas: menos fricción para el primer slice; menos capas vacías.
- Trade-off: `domain` y `application` **no pueden** estar ambos en `agents.active` a la vez que esta fusión (ver [contrato del agente](../../agents/domain-application.md), sección Restricciones).
- Si el consumidor necesita separar capas más adelante, es una decisión de su propio ADR, no un upgrade de este pack.

## Relacionado

| Destino | Por qué |
|---------|---------|
| [Contrato domain-application](../../agents/domain-application.md) | Restricciones exactas de la fusión |
| [vertical-slice-cqrs](../../playbooks/vertical-slice-cqrs.md) | Principio que motiva la fusión |
