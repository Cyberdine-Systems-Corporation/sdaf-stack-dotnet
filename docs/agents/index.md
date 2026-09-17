# Agentes de extensión

Contratos de los agentes que este pack añade sobre `sdaf-core`. Ninguno redefine `specification`, `architecture` o `testing-review` del núcleo.

| Agente | Modo | Rol |
|--------|------|-----|
| [Frontend](frontend.md) | active (si el consumidor lo declara) | UI Blazor + BFF |
| [Domain + Application](domain-application.md) | active (fusión) | Slice dominio + aplicación .NET |
| [Infrastructure](infrastructure.md) | **stub** | Persistencia/adapters bajo demanda humana |

> [!IMPORTANT]
> Gate 0 del core manda sobre cualquier skill de implementación invocada por estos agentes.

## Relacionado

| Destino | Por qué |
|---------|---------|
| [Skills](../skills/index.md) | Flujos operativos que estos agentes invocan |
| [Playbooks](../playbooks/index.md) | Normas técnicas que deben respetar |
| [ADR](../architecture/adr/index.md) | Por qué domain+application está fusionado y por qué infrastructure es stub |
