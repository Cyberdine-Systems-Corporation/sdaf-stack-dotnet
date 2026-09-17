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
- [Sitio navegable (MkDocs)](#sitio-navegable-mkdocs)
- [Validar enlaces](#validar-enlaces)
- [Relacionado](#relacionado)

## Roles de página

| Rol | Dónde | Sustituye constitución? |
|-----|-------|-------------------------|
| Constitución / método | sdaf-core (externo) | — |
| HOWTO adopción | [ADOPT.md](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/blob/main/ADOPT.md) | No |
| Contrato Approved | [agents/](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/tree/main/agents) | No |
| Playbook / norma técnica | [playbooks/](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/tree/main/playbooks) | No (overlay) |
| Skill operativa | [skills/](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/tree/main/skills) | No |
| Prompt / plantilla | [prompts/agents/](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/tree/main/prompts/agents) | No |
| Índice / hub | [README.md](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/blob/main/README.md) | No |

## Tres puertas

Desde el [README](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/blob/main/README.md):

| Puerta | Destino |
|--------|---------|
| 🛠️ Adoptar | [ADOPT.md](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/blob/main/ADOPT.md) |
| 📖 Entender contratos | [agents/](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/tree/main/agents) · [playbooks/](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/tree/main/playbooks) |
| 🛠️ Operar | [skills/README.md](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/blob/main/skills/README.md) |

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

## Sitio navegable (MkDocs)

Este mismo contenido también se sirve como sitio con búsqueda, Mermaid y syntax highlighting vía MkDocs + Material (versionado con `mike`, igual que sdaf-core). URL de desarrollo: [`…/sdaf-stack-dotnet/dev/`](https://cyberdine-systems-corporation.github.io/sdaf-stack-dotnet/dev/). Ver [`docs/uso-local.md`](uso-local.md) y el workflow [`docs.yml`](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/blob/main/.github/workflows/docs.yml).

## Validar enlaces

Falla si un enlace relativo apunta a un archivo inexistente. Avisa anclas dudosas y Markdown huérfanos.

```powershell
pwsh -File ./scripts/check-md-links.ps1
# o, en Windows PowerShell 5.1:
powershell -File ./scripts/check-md-links.ps1
```

CI: [`docs-links.yml`](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/blob/main/.github/workflows/docs-links.yml).

## Relacionado

| Destino | Por qué |
|---------|---------|
| [README.md](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/blob/main/README.md) | Hub y tres puertas |
| [ADOPT.md](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/blob/main/ADOPT.md) | Adopción |
| [CHANGELOG.md](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/blob/main/CHANGELOG.md) | Versiones del pack |
| [skills/README.md](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/blob/main/skills/README.md) | Catálogo operativo |
