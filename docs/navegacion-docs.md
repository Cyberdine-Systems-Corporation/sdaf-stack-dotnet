# Navegación de la documentación

| Campo | Valor |
|--------|--------|
| Rol | 🧭 HOWTO de navegación (no es norma) |
| Pack | `sdaf-stack-dotnet@0.3.0` |

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

> [!TIP]
> DoD de una página markdown: [checklist-pagina-docs.md](checklist-pagina-docs.md).

## Roles de página

| Rol | Dónde | Sustituye constitución? |
|-----|-------|-------------------------|
| Constitución / método | sdaf-core (externo) | — |
| HOWTO adopción | [ADOPT.md](../ADOPT.md) | No |
| Contrato Approved | [agents/](../agents/README.md) | No |
| Playbook / norma técnica | [playbooks/](../playbooks/README.md) | No (overlay) |
| Skill operativa | [skills/](../skills/README.md) | No |
| Prompt / plantilla | `prompts/agents/` (enlazado desde cada [contrato](../agents/README.md)) | No |
| Índice / hub | [README.md](../README.md) | No |

## Tres puertas

Desde el [README](../README.md):

| Puerta | Destino |
|--------|---------|
| 🛠️ Adoptar | [ADOPT.md](../ADOPT.md) |
| 📖 Entender contratos | [agents/](../agents/README.md) · [playbooks/](../playbooks/README.md) |
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

## Sitio navegable (MkDocs)

Este mismo contenido también se sirve como sitio con búsqueda, Mermaid y syntax highlighting vía MkDocs + Material (versionado con `mike`, igual que sdaf-core). URL de desarrollo: [`…/sdaf-stack-dotnet/dev/`](https://cyberdine-systems-corporation.github.io/sdaf-stack-dotnet/dev/). Ver [`docs/uso-local.md`](uso-local.md) y el workflow [`docs.yml`](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/blob/main/.github/workflows/docs.yml).

**Decisión A (look):** palette Material sin `primary` indigo, features mínimas y `slugify_unicode` — mismo contrato visual que sdaf-core. Semántica de iconos/alertas/Mermaid = esta página; no usar iconos `:material-*` en hubs.

**Fuentes:** `docs_dir` es la raíz del repo, como en sdaf-core desde 2026-09-20 (sin symlinks ni páginas espejo). Un enlace relativo vale igual en GitHub y en el sitio, también hacia `CHANGELOG.md`, `pack.yaml` o `.cursor/`. Config: [`mkdocs/mkdocs.yml`](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/blob/main/mkdocs/mkdocs.yml).

## Validar enlaces

Falla si un enlace relativo apunta a un archivo inexistente. Con `-StrictAnchors` falla también por anclas que no existan con el slug de GitHub **y** el de MkDocs (`slugify_unicode`); con `-StrictOrphans`, por Markdown sin enlaces entrantes.

```powershell
pwsh -File ./scripts/check-md-links.ps1 -StrictAnchors -StrictOrphans
# o, en Windows PowerShell 5.1:
powershell -File ./scripts/check-md-links.ps1 -StrictAnchors -StrictOrphans
```

CI: [`docs-links.yml`](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/blob/main/.github/workflows/docs-links.yml), en modo estricto y en todo PR.

## Relacionado

| | Destino | Por qué |
|--|---------|---------|
| 🧭 | [README.md](../README.md) | Hub y tres puertas |
| 🛠️ | [ADOPT.md](../ADOPT.md) | Adopción |
| 📝 | [checklist-pagina-docs.md](checklist-pagina-docs.md) | DoD de página markdown |
| ✅ | [CHANGELOG.md](../CHANGELOG.md) | Versiones del pack |
| 🛠️ | [skills/README.md](../skills/README.md) | Catálogo operativo |
