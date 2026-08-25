# sdaf-stack-dotnet

Pack de stack SDAF para **.NET / Blazor / Aspire**.

| Campo | Valor |
|--------|--------|
| Id | `sdaf-stack-dotnet@0.1.0` |
| Compat | `sdaf-core` **>=0.2.0 &lt;0.3.0** |
| Contrato | [sdaf-core `docs/contrato-pack-stack.md`](https://github.com/Cyberdine-Systems-Corporation/sdaf-core/blob/v0.2.0/docs/contrato-pack-stack.md) |

## Qué aporta

- Skills: `csharp-adr006-slice`, `blazor-bff-slice`, `aspire-local-run`
- Agentes de extensión: `frontend`, `domain-application`, `infrastructure` (stub)
- Playbooks: coding standards C#, vertical slice + CQRS
- Regla IDE fina: `.cursor/rules/coding-standards-csharp.mdc`

## Qué no es

- No es un producto ni una solución `.sln`.
- No sustituye ADRs de stack del consumidor.
- No redefine specification / architecture / testing-review del core.
- No contiene `specs/` ni `knowledge/` de dominio.

## Cómo adoptar

Ver [ADOPT.md](ADOPT.md). Resumen: pin a tag `v0.1.0`, declarar `stack.pack: sdaf-stack-dotnet@0.1.0` con `sdaf.version: "0.2.0"`, materializar agentes/skills del pack.

## Familia sdaf-stack-*

Otros packs (node, etc.) deben repetir este patrón: `pack.yaml`, agentes solo de extensión, skills con prefijo de stack, `ADOPT.md`, sin producto. Este repo es el primer ejemplar.

## Licencia

MIT — ver [LICENSE](LICENSE).
