# Adopción — sdaf-stack-dotnet@0.1.0

Requiere **sdaf-core@0.2.x** ya adoptado (submodule/copia) y Gate 0 del método vigente.

## Pasos

1. Añadir este pack como submodule pinneado a tag `v0.1.0`, p. ej. en `sdaf-stack-dotnet/`:

```text
git submodule add <url-sdaf-stack-dotnet> sdaf-stack-dotnet
cd sdaf-stack-dotnet && git checkout v0.1.0
```

2. En la raíz del consumidor, `sdaf.config.yaml`:

```yaml
sdaf:
  version: "0.2.0"
stack:
  pack: sdaf-stack-dotnet@0.1.0
```

3. Materializar (copiar o enlazar) desde el pack hacia el consumidor:

- `agents/frontend-agent.md`, `domain-application-agent.md`, `infrastructure-agent.md`
- `prompts/agents/` correspondientes
- `skills/csharp-adr006-slice`, `blazor-bff-slice`, `aspire-local-run`
- Opcional: playbooks y `.cursor/rules/coding-standards-csharp.mdc`

4. Elegir escenario de [`examples/`](examples/):

- `01-pack-only.yaml` — playbooks sin cambiar activos del core
- `02-pack-frontend.yaml` — activa `domain-application` + `frontend`

5. Si el runtime/UI/BD se fijan por primera vez: abrir **ADR** en el consumidor (el pack no sustituye esa decisión).

6. Antes de código de producto: skill `sdaf-gate0` del core.

## Prohibido

- Declarar este pack como constitución del método.
- Saltar Gate 0 “porque hay skill csharp”.
- Meter dominio o specs de un producto dentro del pack.

## Upgrade

Al subir el tag del pack: actualizar pin, `stack.pack` semver, y citas `skill@version` en worklogs nuevos. No auto-migrar specs del consumidor.
