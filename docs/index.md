# sdaf-stack-dotnet

Sitio navegable (MkDocs + Material) sobre el pack **`sdaf-stack-dotnet`**. Renderiza los mismos artefactos Approved del repo — no los duplica ni los reinterpreta.

> [!NOTE]
> Este sitio es una capa de **lectura** (búsqueda, navegación, syntax highlighting, Mermaid). La constitución del método sigue viviendo en `sdaf-core`; este pack sigue siendo overlay. Ver [`README.md`](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/blob/main/README.md) del repo para el hub canónico en GitHub.

## Tres puertas

| Puerta | Destino | Para quién |
|--------|---------|------------|
| :material-wrench: Adoptar el pack | [Adopción](adoption/index.md) | Quien materializa submodule, `sdaf.config.yaml` y enlaces |
| :material-book-open-variant: Entender contratos | [Agentes](agents/index.md) · [Playbooks](playbooks/index.md) | Quien aplica norma del overlay |
| :material-hammer-wrench: Operar el día a día | [Skills](skills/index.md) | Quien ejecuta slices, UI/BFF o runtime local |

## Qué encontrarás aquí

- **Arquitectura** — cómo se relacionan `pack.yaml`, agentes, skills y playbooks con `sdaf-core`, y las decisiones de diseño del propio pack ([ADR](architecture/adr/index.md)).
- **Agentes** — contratos de extensión (`frontend`, `domain-application`, `infrastructure`).
- **Skills** — HOWTO operativos con sus flujos Mermaid (`csharp-adr006-slice`, `blazor-bff-slice`, `aspire-local-run`).
- **Playbooks** — normas técnicas de stack (`coding-standards-csharp`, `vertical-slice-cqrs`).
- **Adopción** — pasos para pinnear el pack como submodule y elegir un escenario de `examples/`.

## Qué no es

- No es la constitución del método (eso vive en `sdaf-core`).
- No sustituye ADRs de stack del **consumidor** del pack.
- No contiene `specs/` ni `knowledge/` de dominio de un producto.

## Relacionado

| Destino | Por qué |
|---------|---------|
| [Uso local](uso-local.md) | Levantar este sitio en tu máquina |
| [Navegación](navegacion-docs.md) | Vocabulario visual y mapa de clics del repo en GitHub |
| [Arquitectura](architecture/index.md) | Relación entre componentes del pack |
