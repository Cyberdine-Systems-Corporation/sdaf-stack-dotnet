# Playbook — Coding standards C#

| Campo | Valor |
|--------|--------|
| Rol | 📖 Playbook / norma técnica de stack |
| Versión | 0.1.1 |
| Pack | sdaf-stack-dotnet@0.1.1 |
| Estado | Approved |
| Fecha | 2026-08-25 |

> [!NOTE]
> Norma técnica del **overlay**. No sustituye el handbook Approved de sdaf-core ni el ADR de coding standards del consumidor.

## En esta página

- [Alcance](#alcance)
- [Normas](#normas)
- [Relación con la regla IDE](#relación-con-la-regla-ide)
- [Relacionado](#relacionado)

## Alcance

Convenciones de código C# / .NET para consumidores de este pack. El ADR de coding standards del consumidor puede endurecer o sustituir puntos; no contradecir sdaf-core.

## Normas

| # | Norma |
|---|--------|
| 1 | Nombres claros; ubiquitous language de las specs en tipos de dominio. |
| 2 | Preferir código explícito a magia; async con `Async` suffix en métodos públicos async. |
| 3 | No capturar excepciones vacías; fallar de forma observable en límites de aplicación. |
| 4 | Nullable reference types on; evitar `!` salvo justificación local. |
| 5 | Secretos solo fuera del repo (user secrets / variables de entorno). |
| 6 | Tests en el proyecto de tests del consumidor (`tests_path`); nombres que reflejen acceptance. |
| 7 | Commits y worklogs en castellano (regla SDAF); identificadores de código en inglés técnico salvo que el ADR diga lo contrario. |

## Relación con la regla IDE

La regla [`.cursor/rules/coding-standards-csharp.mdc`](../.cursor/rules/coding-standards-csharp.mdc) resume lo anterior sin duplicar el handbook del método.

## Relacionado

| Destino | Por qué |
|---------|---------|
| [vertical-slice-cqrs.md](vertical-slice-cqrs.md) | Cómo estructurar el slice |
| [../skills/csharp-adr006-slice/SKILL.md](../skills/csharp-adr006-slice/SKILL.md) | Flujo operativo del slice |
| [../.cursor/rules/coding-standards-csharp.mdc](../.cursor/rules/coding-standards-csharp.mdc) | Resumen IDE |
| [../README.md](../README.md) | Hub del pack |
