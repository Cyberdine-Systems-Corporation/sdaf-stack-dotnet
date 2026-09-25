# ADR-001 — Fusión `domain-application`

| Campo | Valor |
|--------|--------|
| Estado | Aceptado |
| Fecha | 2026-09-13 |
| Decisores | No constan en el texto publicado. Autor del fichero: Manuel Ortiz de Villajos Quirós (commit `c9517a9`). |
| Aceptación | Publicado con estado `Approved` en el merge del PR #4 (`ae2df53`, 2026-09-17, por @mortiz-iadev, identidad de [`CODEOWNERS`](../../../CODEOWNERS)) y en el tag `v0.2.0`. La hora no consta. En 0.3.0 solo cambian el vocabulario del estado (`Approved` → `Aceptado`, como en sdaf-core) y la numeración (`ADR-0001` → `ADR-001`); no es una aceptación nueva. |
| Vigente en | `sdaf-stack-dotnet@0.3.0` (desde 0.1.0) |

## Contexto

Un pack de stack para MVPs en .NET no necesita, desde el día uno, separar los agentes `domain` y `application` del núcleo SDAF: montar ambas capas vacías "para el futuro" contradice el principio de vertical slice (ver [`playbooks/vertical-slice-cqrs.md`](../../../playbooks/vertical-slice-cqrs.md)).

## Decisión

Se define un único agente de extensión **`domain-application`** (fusión) que implementa dominio + aplicación como un solo slice, invocando la skill [`csharp-adr006-slice`](../../../skills/csharp-adr006-slice/SKILL.md). La separación de capas solo ocurre si un ADR del **consumidor** la exige explícitamente.

## Alternativas consideradas

- Dos agentes independientes (`domain`, `application`) activos desde 0.1.0 — descartada: añade ceremonia sin PBI que la justifique en un MVP.
- Sin agente propio, delegando todo a `sdaf-core` — descartada: el core no conoce las convenciones C#/.NET del stack (naming, nullable, async).

## Consecuencias

- Positivas: menos fricción para el primer slice; menos capas vacías.
- Trade-off: `domain` y `application` **no pueden** estar ambos en `agents.active` a la vez que esta fusión (ver [contrato del agente](../../../agents/domain-application-agent.md), sección Restricciones).
- Si el consumidor necesita separar capas más adelante, es una decisión de su propio ADR, no un upgrade de este pack.

## Relacionado

| | Destino | Por qué |
|--|---------|---------|
| 🧭 | [Contrato domain-application](../../../agents/domain-application-agent.md) | Restricciones exactas de la fusión |
| 📖 | [vertical-slice-cqrs](../../../playbooks/vertical-slice-cqrs.md) | Principio que motiva la fusión |
