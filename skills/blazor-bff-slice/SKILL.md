---
name: blazor-bff-slice
description: Implementa un slice UI Blazor y/o BFF según specs Approved. Usar con agente frontend tras Gate 0.
---

<!-- --8<-- [start:cuerpo] -->
# blazor-bff-slice

| Campo | Valor |
|--------|--------|
| Rol | 🛠️ Skill / HOWTO operativo |
| ID | blazor-bff-slice |
| Versión | 0.1.1 |
| Estado | Approved |
| Prioridad | alta |
| Fecha | 2026-08-25 |
| Pack | sdaf-stack-dotnet@0.1.1 |
| Norma | playbooks/coding-standards-csharp.md, ADRs UI/API del consumidor, Gate 0 |

> [!NOTE]
> HOWTO de UI/BFF. **BFF** = Backend-for-Frontend: capa API orientada a la UI, no al dominio expuesto crudo.

## En esta página

- [Disparadores](#disparadores)
- [Pasos](#pasos)
- [Definition of Done](#definition-of-done)
- [Restricciones](#restricciones)
- [Relacionado](#relacionado)
- [Historial](#historial)

## Disparadores

- PBI de pantalla/flujo UI; “añadir BFF endpoint para la UI”.
- Agente `frontend` activo.

## Pasos

```mermaid
flowchart TD
  g0[Confirmar Gate 0] --> adr[Respetar límites BFF/API]
  adr --> ui[Implementar Blazor + BFF]
  ui --> reuse[Reutilizar contratos de aplicación]
  reuse --> wl[Registrar skill@0.1.1]
  domainUi[Reglas de dominio en UI] --> stop[STOP]

  classDef stop fill:#f8d0d0,stroke:#8b1e1e,color:#8b1e1e
  classDef ok fill:#d4edda,stroke:#2d6a4f,color:#2d6a4f
  classDef stub fill:#e9ecef,stroke:#6c757d,color:#6c757d
  classDef core fill:#d0e3f8,stroke:#1e4d8b,color:#1e4d8b

  class stop stop
  class wl ok
  class g0 core
  class domainUi stop
```

1. Confirmar Gate 0 y acceptance UI.
2. Respetar límites BFF/API del ADR del consumidor (no llamar dominio desde el browser si el ADR lo prohíbe).
3. Implementar componentes/páginas Blazor y endpoints BFF necesarios en `src_path`.
4. Reutilizar contratos ya expuestos por el slice de aplicación; no duplicar reglas de negocio en la UI.
5. Citar `blazor-bff-slice@0.1.1` en worklog; handoff a testing-review.

## Definition of Done

- [ ] ✅ Flujo UI del In observable según acceptance
- [ ] ✅ Sin lógica de dominio nueva en la UI
- [ ] ✅ Worklog cerrado

## Restricciones

> [!WARNING]
> ⛔ No Gate 0 skip; no secretos en cliente.

Framework concreto lo fija el ADR del consumidor (este skill asume Blazor como playbook del pack).

<!-- --8<-- [end:cuerpo] -->

## Relacionado

| | Destino | Por qué |
|--|---------|---------|
| 🧭 | [../../agents/frontend-agent.md](../../agents/frontend-agent.md) | Contrato que invoca esta skill |
| 📖 | [../../playbooks/coding-standards-csharp.md](../../playbooks/coding-standards-csharp.md) | Estándares C# |
| 🧭 | [../README.md](../README.md) | Índice de skills |

## Historial

| Versión | Fecha | Cambio |
|---------|--------|--------|
| 0.1.0 | 2026-08-25 | Primera versión del pack |
| 0.1.1 | 2026-09-17 | Alineación pack@0.1.1; TOC/Relacionado/Mermaid |
