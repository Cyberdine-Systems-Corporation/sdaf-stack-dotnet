# Navegación de la documentación

| Campo | Valor |
|--------|--------|
| Rol | 🧭 HOWTO de navegación (no es norma) |
| Pack | `sdaf-stack-dotnet@0.1.1` |

> [!NOTE]
> Mapa de clics y vocabulario visual. No sustituye contratos Approved, playbooks ni sdaf-core.

## En esta página

- [Roles de página](#roles-de-página)
- [Tres puertas](#tres-puertas)
- [Mapa de clics](#mapa-de-clics)
- [Vocabulario visual](#vocabulario-visual)
- [Validar enlaces](#validar-enlaces)
- [Relacionado](#relacionado)

## Roles de página

| Rol | Dónde | Sustituye constitución? |
|-----|-------|-------------------------|
| Constitución / método | sdaf-core (externo) | — |
| HOWTO adopción | [ADOPT.md](../ADOPT.md) | No |
| Contrato Approved | [agents/](../agents/) | No |
| Playbook / norma técnica | [playbooks/](../playbooks/) | No (overlay) |
| Skill operativa | [skills/](../skills/) | No |
| Prompt / plantilla | [prompts/agents/](../prompts/agents/) | No |
| Índice / hub | [README.md](../README.md) | No |

## Tres puertas

Desde el [README](../README.md):

| Puerta | Destino |
|--------|---------|
| 🛠️ Adoptar | [ADOPT.md](../ADOPT.md) |
| 📖 Entender contratos | [agents/](../agents/) · [playbooks/](../playbooks/) |
| 🛠️ Operar | [skills/README.md](../skills/README.md) |

## Mapa de clics

Clics desde el README (objetivo ≤3):

| Tarea | Clics | Ruta |
|-------|------:|------|
| Adoptar el pack | 1 | README → ADOPT |
| Listar skills | 1 | README → skills/README |
| Abrir skill csharp | 2 | README → skills/README → SKILL |
| Contrato frontend | 1–2 | README → agents/frontend-agent |
| Playbook vertical slice | 1–2 | README → playbooks/vertical-slice-cqrs |
| Estándares C# | 1–2 | README → playbooks/coding-standards-csharp |
| Escenarios examples | 2 | README → ADOPT → examples |
| Vocabulario visual | 1 | README → esta página |
| Validar enlaces | 1 | comando abajo |

## Vocabulario visual

### Iconos (cerrado)

| Icono | Rol |
|-------|-----|
| 📖 | Constitución / norma |
| 🛠️ | HOWTO / playbook operativo |
| ⛔ | STOP / gate |
| ✅ | Vigente / DoD / proceed |
| 📝 | Borrador / plantilla |
| 📦 | Extensión / pack / plugin |
| 🧭 | Navegación / Relacionado |

Si no encaja, no pongas icono. Cero emoji en headings de páginas normativas (contratos/playbooks).

### Alertas GFM

| Alerta | Uso |
|--------|-----|
| `NOTE` | Esto es HOWTO / no es la constitución |
| `TIP` | Camino recomendado |
| `WARNING` | Prohibición operativa |
| `CAUTION` | STOP / no continuar |
| `IMPORTANT` | Principio que no se puede ignorar |

### Mermaid (clases fijas)

| Clase | Fondo / trazo | Significado |
|-------|---------------|-------------|
| stop | `#f8d0d0` / `#8b1e1e` | STOP |
| ok | `#d4edda` / `#2d6a4f` | Approved / listo |
| stub | `#e9ecef` / `#6c757d` | stub / derivado |
| core | `#d0e3f8` / `#1e4d8b` | nivel constitucional / core |

## Validar enlaces

Falla si un enlace relativo apunta a un archivo inexistente. Avisa anclas dudosas y Markdown huérfanos.

```powershell
pwsh -File ./scripts/check-md-links.ps1
# o, en Windows PowerShell 5.1:
powershell -File ./scripts/check-md-links.ps1
```

CI: [`.github/workflows/docs-links.yml`](../.github/workflows/docs-links.yml).

## Relacionado

| Destino | Por qué |
|---------|---------|
| [../README.md](../README.md) | Hub y tres puertas |
| [../ADOPT.md](../ADOPT.md) | Adopción |
| [../CHANGELOG.md](../CHANGELOG.md) | Versiones del pack |
| [../skills/README.md](../skills/README.md) | Catálogo operativo |
