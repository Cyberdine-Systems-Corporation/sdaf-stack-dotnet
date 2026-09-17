# Arquitectura del pack

`sdaf-stack-dotnet` es un **overlay técnico**: no define runtime, UI ni base de datos por norma (eso lo fija el ADR del consumidor). Lo que sí define es el conjunto de contratos, skills y playbooks que un consumidor .NET/Blazor/Aspire materializa sobre `sdaf-core`.

## Árbol del pack

```text
sdaf-stack-dotnet/
├── README.md                 ← hub
├── ADOPT.md                  ← HOWTO adopción
├── pack.yaml                 ← manifest
├── CHANGELOG.md
├── docs/                     ← este sitio + navegacion-docs.md
├── agents/                   ← contratos de extensión
├── prompts/agents/           ← prompts de sistema
├── playbooks/                ← norma técnica del stack
├── skills/                   ← playbooks operativos por skill
├── examples/                 ← escenarios sdaf.config
└── .cursor/rules/            ← regla IDE fina C#
```

## Relación con sdaf-core

- El pack declara compatibilidad `sdaf_core: ">=0.2.0 <0.3.0"` en [`pack.yaml`](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/blob/main/pack.yaml).
- Gate 0 y el handbook Approved viven en `sdaf-core`; este pack solo aporta agentes de **extensión** (nunca redefine `specification`, `architecture` o `testing-review` del core).
- El consumidor materializa el pack como submodule pinneado a un tag — ver [Adopción](../adoption/index.md).

## Ver también

- [Relación de componentes](relacion-componentes.md) — diagrama de cómo se conectan agentes, skills y playbooks.
- [Decisiones (ADR)](adr/index.md) — decisiones de diseño del propio pack.

## Relacionado

| Destino | Por qué |
|---------|---------|
| [Agentes](../agents/index.md) | Contratos que consumen esta arquitectura |
| [Skills](../skills/index.md) | Flujos operativos concretos |
| [Adopción](../adoption/index.md) | Cómo se instala este árbol en un consumidor |
