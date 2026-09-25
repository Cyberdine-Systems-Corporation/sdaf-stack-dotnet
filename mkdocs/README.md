# mkdocs/

Sitio Material del pack. Mismo modelo que `sdaf-core/mkdocs/`:

| Ruta | Rol |
|------|-----|
| `mkdocs.yml` | Config Material + `mike` (Decisión A). `docs_dir: ..` = raíz del repo; `exclude_docs` deja fuera el tooling |

Build: `mkdocs build -f mkdocs/mkdocs.yml --strict` — ver [`docs/uso-local.md`](../docs/uso-local.md).
