# Escenarios de `examples/`

| Campo | Valor |
|--------|--------|
| Rol | 🛠️ HOWTO de escenarios de config |
| Pack | `sdaf-stack-dotnet@0.4.0` |

Cada escenario es un `sdaf.config.yaml` de referencia a copiar en la raíz del consumidor y ajustar (`project.name`, `stack.src_path`, `stack.tests_path`).

## En esta página

- [`01-pack-only.yaml`](#01-pack-onlyyaml-playbooks-sin-activar-agentes-de-extensión)
- [`02-pack-frontend.yaml`](#02-pack-frontendyaml-activa-domain-application-y-frontend)
- [Validación](#validación)
- [Relacionado](#relacionado)

## `01-pack-only.yaml`: playbooks sin activar agentes de extensión

```yaml
--8<-- "examples/01-pack-only.yaml"
```

Uso: adoptar solo playbooks/skills del pack manteniendo el modelo de agentes por defecto de `sdaf-core` (`specification`, `architecture`, `testing-review` activos; el resto en stub).

## `02-pack-frontend.yaml`: activa `domain-application` y `frontend`

```yaml
--8<-- "examples/02-pack-frontend.yaml"
```

Uso: handoff completo `Specification → Architecture → domain-application → frontend ↘ testing-review ↗`. Activa la fusión documentada en [ADR-001](../architecture/adr/ADR-001-fusion-domain-application.md).

`domain` y `application` aparecen en `stubs` y a la vez como miembros de la fusión: no se activan por separado, solo a través de `domain-application`. Tenerlos en `agents.active` junto con la fusión incumple el [contrato](../../agents/domain-application-agent.md#restricciones).

## Validación

Los dos escenarios se validan en el CI del pack con la composite action `validate-sdaf` del core (schema + invariantes, I4 en modo estricto), fijada a un SHA de `main` del core hasta que exista el tag `v0.6.0`. En local, con un checkout del core al lado, también contra el manifiesto del pack:

```powershell
python ../sdaf-core/scripts/validate-pack.py sdaf-pack.yaml
python ../sdaf-core/scripts/validate-config.py --strict-i4 --consumer-root . --pack-manifest sdaf-pack.yaml examples/01-pack-only.yaml examples/02-pack-frontend.yaml
```

## Relacionado

| | Destino | Por qué |
|--|---------|---------|
| 🛠️ | [ADOPT.md](../../ADOPT.md) | Pasos completos de materialización |
| 📦 | [ADR-001](../architecture/adr/ADR-001-fusion-domain-application.md) | Por qué domain+application se activa fusionado |
| 🧭 | [README.md](../../README.md) | Hub del pack |
