# Escenarios de `examples/`

| Campo | Valor |
|--------|--------|
| Rol | 🛠️ HOWTO de escenarios de config |
| Pack | `sdaf-stack-dotnet@0.2.0` |

Cada escenario es un `sdaf.config.yaml` de referencia a copiar en la raíz del consumidor y ajustar (`project.name`, `stack.src_path`, `stack.tests_path`).

## `01-pack-only.yaml` — playbooks sin activar agentes de extensión

```yaml
--8<-- "examples/01-pack-only.yaml"
```

Uso: adoptar solo playbooks/skills del pack manteniendo el modelo de agentes por defecto de `sdaf-core` (`specification`, `architecture`, `testing-review` activos; el resto en stub).

## `02-pack-frontend.yaml` — activa `domain-application` + `frontend`

```yaml
--8<-- "examples/02-pack-frontend.yaml"
```

Uso: handoff completo `Specification → Architecture → domain-application → frontend ↘ testing-review ↗`. Activa la fusión documentada en [ADR-0001](../architecture/adr/0001-fusion-domain-application.md).

## Relacionado

| | Destino | Por qué |
|--|---------|---------|
| 🛠️ | [ADOPT.md](../../ADOPT.md) | Pasos completos de materialización |
| 📦 | [ADR-0001](../architecture/adr/0001-fusion-domain-application.md) | Por qué domain+application se activa fusionado |
| 🧭 | [README.md](../../README.md) | Hub del pack |
