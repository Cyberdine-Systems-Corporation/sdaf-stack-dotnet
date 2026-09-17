# Skills

HOWTO operativos del pack. Cita `skill-id@version` en worklogs (p. ej. `csharp-adr006-slice@0.1.1`). Gate 0 del core manda sobre cualquier skill de implementación.

| Skill | Prioridad | Agente que la invoca |
|-------|-----------|------------------------|
| [csharp-adr006-slice](csharp-adr006-slice.md) | alta | [domain-application](../agents/domain-application.md) |
| [blazor-bff-slice](blazor-bff-slice.md) | alta | [frontend](../agents/frontend.md) |
| [aspire-local-run](aspire-local-run.md) | media | onboarding / Gate 2 |

## Relacionado

| Destino | Por qué |
|---------|---------|
| [Playbooks](../playbooks/index.md) | Normas que estas skills deben respetar |
| [Agentes](../agents/index.md) | Contratos que invocan estas skills |
