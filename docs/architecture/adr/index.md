# Decisiones de diseño (ADR)

Estos ADR documentan decisiones de diseño **del propio pack** `sdaf-stack-dotnet` (por qué se modela así el conjunto de agentes/skills/playbooks). No sustituyen ni prescriben los ADR de stack que cada **consumidor** debe abrir para su runtime, UI o base de datos concretos — ver [ADOPT.md](../../../ADOPT.md).

## Índice

| ADR | Título | Estado |
|-----|--------|--------|
| [ADR-001](ADR-001-fusion-domain-application.md) | Fusión `domain-application` | Aceptado |
| [ADR-002](ADR-002-infrastructure-stub.md) | `infrastructure` como agente stub | Aceptado |

Numeración desde 001, como sdaf-core. Hasta el tag `v0.2.0` se llamaban `ADR-0001` y `ADR-0002` (ficheros `0001-…` y `0002-…`). Aceptar un ADR es un acto humano de la identidad de [`CODEOWNERS`](../../../CODEOWNERS); un agente no cambia el estado.

Usa la [plantilla](plantilla-adr.md) para proponer nuevos ADR del pack.

## Relacionado

| | Destino | Por qué |
|--|---------|---------|
| 📦 | [Arquitectura](../index.md) | Contexto general del pack |
| 📦 | [Relación de componentes](../relacion-componentes.md) | Diagrama que estas decisiones explican |
