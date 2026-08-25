# Playbook — Vertical slice + CQRS (aplicación)

| Campo | Valor |
|--------|--------|
| Versión | 0.1.0 |
| Pack | sdaf-stack-dotnet@0.1.0 |
| Estado | Approved |
| Fecha | 2026-08-25 |

## Idea

Un PBI In se entrega como **vertical slice**: un caso de uso (comando o consulta) atraviesa los límites necesarios sin montar capas vacías “para el futuro”.

## Pasos conceptuales

1. Nombrar el use case desde la spec de aplicación.
2. Separar **comando** (cambia estado) vs **consulta** (lee) cuando aporte claridad (CQRS ligero).
3. Invariantes de dominio cerca del modelo; orquestación en aplicación.
4. Puertos/adapters solo si el ADR de infraestructura lo exige (el agente infrastructure es stub en 0.1.0).
5. Acceptance → tests antes o junto al código (Test from Specs).

## Anti-patrones

- God services que mezclan todos los PBI.
- Exponer el modelo de dominio crudo por HTTP sin DTO/contrato acordado.
- UI que reimplementa reglas hard de dominio.

## Skill asociada

`csharp-adr006-slice@0.1.0`
