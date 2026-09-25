# Agentes de extensión

| Campo | Valor |
|--------|--------|
| Rol | 🧭 Índice de contratos del pack |
| Pack | `sdaf-stack-dotnet@0.3.0` |

Contratos de los agentes que este pack añade sobre `sdaf-core`. Ninguno redefine `specification`, `architecture` o `testing-review` del núcleo.

| Agente | Modo | Rol |
|--------|------|-----|
| [Frontend](frontend-agent.md) | active (si el consumidor lo declara) | UI Blazor + BFF |
| [Domain + Application](domain-application-agent.md) | active (fusión) | Slice dominio + aplicación .NET |
| [Infrastructure](infrastructure-agent.md) | **stub** | Persistencia/adapters bajo demanda humana |

«Activo» significa listado en `agents.active` del `sdaf.config.yaml` del consumidor. Con `stack.pack` declarado, el validador del core acepta estos ids de extensión (invariante I4); ver los [escenarios](../docs/adoption/escenarios.md).

> [!IMPORTANT]
> Gate 0 del core manda sobre cualquier skill de implementación invocada por estos agentes.

## Relacionado

| | Destino | Por qué |
|--|---------|---------|
| 🛠️ | [../skills/README.md](../skills/README.md) | Flujos operativos que estos agentes invocan |
| 📖 | [../playbooks/README.md](../playbooks/README.md) | Normas técnicas que deben respetar |
| 📦 | [../docs/architecture/adr/index.md](../docs/architecture/adr/index.md) | Por qué domain+application está fusionado y infrastructure es stub |
| 🧭 | [../README.md](../README.md) | Hub del pack |
