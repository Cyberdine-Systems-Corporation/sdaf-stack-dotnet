<!-- --8<-- [start:cuerpo] -->
# Adopción — sdaf-stack-dotnet@0.3.0

| Campo | Valor |
|--------|--------|
| Rol | 🛠️ HOWTO de adopción (no es constitución del método) |
| Pack | `sdaf-stack-dotnet@0.3.0` |
| Requiere | `sdaf-core@0.4.x` ya adoptado (pin `v0.4.2` recomendado) + Gate 0 del método vigente |

> [!NOTE]
> Esto es un **HOWTO**. No sustituye el handbook Approved ni la constitución de **sdaf-core**.

## En esta página

- [Flujo](#flujo)
- [Pasos](#pasos)
- [Tooling externo (opcional)](#tooling-externo-opcional)
- [Prohibido](#prohibido)
- [Upgrade](#upgrade)
- [Relacionado](#relacionado)

## Flujo

```mermaid
flowchart TD
  pin[Pin submodule v0.3.0] --> cfg[sdaf.config.yaml]
  cfg --> mat[Materializar enlaces]
  mat --> ex[Elegir examples]
  ex --> adr{ADR stack nuevo?}
  adr -->|sí| openAdr[Abrir ADR consumidor]
  adr -->|no| gate0[Gate 0 core]
  openAdr --> gate0
  gate0 --> ready[Listo para código]
  skip[Saltar Gate 0] --> stop[STOP]

  classDef stop fill:#f8d0d0,stroke:#8b1e1e,color:#8b1e1e
  classDef ok fill:#d4edda,stroke:#2d6a4f,color:#2d6a4f
  classDef stub fill:#e9ecef,stroke:#6c757d,color:#6c757d
  classDef core fill:#d0e3f8,stroke:#1e4d8b,color:#1e4d8b

  class stop stop
  class ready ok
  class skip stop
  class gate0 core
```

## Pasos

1. Añadir este pack como submodule pinneado a tag `v0.3.0`, p. ej. en `sdaf-stack-dotnet/`:

    ```text
    git submodule add <url-sdaf-stack-dotnet> sdaf-stack-dotnet
    cd sdaf-stack-dotnet && git checkout v0.3.0
    ```

2. En la raíz del consumidor, `sdaf.config.yaml`:

    ```yaml
    sdaf:
      version: "0.4.0"
    stack:
      pack: sdaf-stack-dotnet@0.3.0
    ```

    Pin del **core**: tag `v0.4.2` (recomendado; `v0.4.0` y `v0.4.1` también valen). `sdaf.version` nombra la línea de constitución (`"0.4.0"`), no un tag — igual que documenta sdaf-core.

3. Materializar aportes del pack en la raíz del consumidor. Preferido: symlinks relativos (Git mode `120000`), no copias.

    En repos de referencia (p. ej. [ShiftFlow-sdaf](https://github.com/Cyberdine-Systems-Corporation/ShiftFlow-sdaf)) hay un script documentado:

    ```powershell
    git submodule update --init --recursive
    git config core.symlinks true
    .\scripts\materialize-submodules.ps1 -Force
    ```

    El HOWTO vive en `docs/materializacion-submodules.md` del **consumidor**. Puedes copiar `scripts/materialize-submodules.ps1` / `.sh` al adoptar el pack; el manifiesto incluye rutas del pack y del core.

    **Fallback manual** (copiar o `ln -s` / `New-Item SymbolicLink`):

    | Consumidor | Origen (relativo desde el padre del enlace) |
    |------------|---------------------------------------------|
    | `agents/frontend-agent.md`, `domain-application-agent.md`, `infrastructure-agent.md` | `../sdaf-stack-dotnet/agents/…` |
    | `prompts/agents/` (mismos ids) | `../../sdaf-stack-dotnet/prompts/agents/…` |
    | `skills/csharp-adr006-slice`, `blazor-bff-slice`, `aspire-local-run` | `../sdaf-stack-dotnet/skills/<id>` |
    | `.cursor/rules/coding-standards-csharp.mdc` (opcional) | `../../sdaf-stack-dotnet/.cursor/rules/coding-standards-csharp.mdc` |

    ⛔ **No** usar junctions de Windows (`mklink /J`): Git no los modela como enlaces portables cross-platform.

    Materializar también skills/agentes/prompts del **core** según [`sdaf-core` docs/adopcion-y-upgrade.md](https://github.com/Cyberdine-Systems-Corporation/sdaf-core/blob/v0.4.2/docs/adopcion-y-upgrade.md).

4. Elegir escenario de `examples/` ([detalle](docs/adoption/escenarios.md)):

    | Escenario | Uso |
    |-----------|-----|
    | `01-pack-only.yaml` | Playbooks sin cambiar activos del core |
    | `02-pack-frontend.yaml` | Activa `domain-application` + `frontend` |

5. Si el runtime/UI/BD se fijan por primera vez: abrir **ADR** en el consumidor (el pack no sustituye esa decisión).

6. Opcional: validar `sdaf.config.yaml` en el CI del consumidor con la composite action [`validate-sdaf`](https://github.com/Cyberdine-Systems-Corporation/sdaf-core/blob/v0.4.2/.github/actions/validate-sdaf/README.md) del core (este pack la usa para sus `examples/`).

7. Antes de código de producto: skill `sdaf-gate0` del core.

> [!IMPORTANT]
> Con **sdaf-core 0.4.x**, H06 §7 exige petición humana **explícita en el mensaje de este turno** para commit o escritura al remoto. El pack no la relaja: no autorices git/remoto desde skills o prompts del overlay.

## Tooling externo (opcional)

El pack no aporta ni presupone tooling de agentes (memoria, MCP, instaladores como gentle-ai). Según [ADR-004](https://github.com/Cyberdine-Systems-Corporation/sdaf-core/blob/v0.4.2/architecture/decisions/ADR-004-tooling-externo-de-agentes.md) del core, ese tooling no es un pack: se declara en `tooling.gentle_ai` de `sdaf.config.yaml`, nunca en `stack.pack`.

Si el consumidor lo adopta:

- Las skills del pack (`csharp-adr006-slice`, `blazor-bff-slice`, `aspire-local-run`) siguen subordinadas a Gate 0 y a H06 §7. No se usan las skills `sdd-*`.
- `AGENTS.md` lleva la sección «Tooling externo» de `AGENTS.md.template` (core `v0.4.2`).
- Guía del core: [`integracion-gentle-ai.md`](https://github.com/Cyberdine-Systems-Corporation/sdaf-core/blob/v0.4.2/docs/integracion-gentle-ai.md).

## Prohibido

> [!CAUTION]
> ⛔ No continues si pretendes declarar este pack como constitución o saltar Gate 0.

- Declarar este pack como constitución del método.
- Saltar Gate 0 “porque hay skill csharp”.
- Meter dominio o specs de un producto dentro del pack.

## Upgrade

Pack **0.2.0 → 0.3.0** exige core **0.4.x**. Quien siga en core `v0.3.3` se queda en pack `v0.2.0`.

1. Subir antes el **core**: pin `v0.4.2` (o `v0.4.0`/`v0.4.1`) y `sdaf.version: "0.4.0"`, siguiendo las secciones 0.4.0, 0.4.1 y 0.4.2 de [`adopcion-y-upgrade.md`](https://github.com/Cyberdine-Systems-Corporation/sdaf-core/blob/v0.4.2/docs/adopcion-y-upgrade.md) (H13, `CODEOWNERS` para QG-Review, worklogs nuevos con frontmatter).
2. Actualizar pin del submodule del **pack** a `v0.3.0`, `stack.pack: sdaf-stack-dotnet@0.3.0` y citas `skill@version` (`@0.3.0`) en worklogs **nuevos**. Los worklogs ya cerrados no se reescriben.
3. Volver a ejecutar el script de materialización del consumidor (`-Force` / `--force` si cambió el árbol).
4. No auto-migrar specs del consumidor.
5. Revisar handoff a `testing-review` y skills del core Parte III (`testing-review-pr`, `security-review`, `devops-ci-gate`) según el escenario.

Los contratos, skills y playbooks no cambian de obligación en 0.3.0: ver [CHANGELOG](CHANGELOG.md).

<!-- --8<-- [end:cuerpo] -->

## Relacionado

| | Destino | Por qué |
|--|---------|---------|
| 🧭 | [README.md](README.md) | Hub y tres puertas |
| 📦 | [Escenarios examples/](docs/adoption/escenarios.md) | Escenarios de configuración |
| 🛠️ | [skills/README.md](skills/README.md) | Skills a materializar |
| 🧭 | [docs/navegacion-docs.md](docs/navegacion-docs.md) | Mapa de clics del pack |
| 📝 | [docs/checklist-pagina-docs.md](docs/checklist-pagina-docs.md) | DoD de página markdown |
| 📦 | [pack.yaml](pack.yaml) | Manifest canónico |
