# ADR-002 — `infrastructure` como agente stub

| Campo | Valor |
|--------|--------|
| Estado | Aceptado |
| Fecha | 2026-09-13 |
| Decisores | No constan en el texto publicado. Autor del fichero: Manuel Ortiz de Villajos Quirós (commit `c9517a9`). |
| Aceptación | Publicado con estado `Approved` en el merge del PR #4 (`ae2df53`, 2026-09-17, por @mortiz-iadev, identidad de [`CODEOWNERS`](../../../CODEOWNERS)) y en el tag `v0.2.0`. La hora no consta. En 0.3.0 solo cambian el vocabulario del estado (`Approved` → `Aceptado`, como en sdaf-core) y la numeración (`ADR-0002` → `ADR-002`); no es una aceptación nueva. |
| Vigente en | `sdaf-stack-dotnet@0.3.0` (desde 0.1.0) |

## Contexto

No todo consumidor de este pack necesita puertos/adapters de persistencia explícitos en su MVP; el playbook [`vertical-slice-cqrs.md`](../../../playbooks/vertical-slice-cqrs.md) ya establece que "puertos/adapters solo si el ADR de infraestructura lo exige". Definir `infrastructure` como agente activo por defecto obligaría a modelar una capa que muchos PBI no necesitan.

## Decisión

`infrastructure` se publica como agente de extensión en **modo stub**: contrato + prompt base existen, pero no se activa por defecto y no forma parte del handoff canónico 0.1.x. Se activa solo bajo **encargo humano explícito**.

## Alternativas consideradas

- Agente `infrastructure` activo por defecto — descartada: fuerza abstracciones de puertos/adapters antes de que el PBI lo pida.
- No publicar el contrato hasta que exista demanda real — descartada: dejaría sin contrato documentado el día que sí se necesite, rompiendo trazabilidad.

## Consecuencias

- Positivas: el flujo canónico (`specification → architecture → domain-application → [frontend] → testing-review`) no arrastra una capa sin uso.
- Trade-off: si un PBI sí requiere infraestructura desacoplada, requiere activación humana explícita y Gate 0 antes de tocar producto.
- El nombre y contrato quedan listos para desacople futuro sin rediseñar el pack.

## Relacionado

| | Destino | Por qué |
|--|---------|---------|
| 🧭 | [Contrato infrastructure](../../../agents/infrastructure-agent.md) | Restricciones del modo stub |
| 📖 | [vertical-slice-cqrs](../../../playbooks/vertical-slice-cqrs.md) | Regla que origina el stub |
