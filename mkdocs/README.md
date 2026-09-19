# mkdocs/

Sitio Material del pack. Misma idea que `sdaf-core/mkdocs/`:

| Ruta | Rol |
|------|-----|
| `mkdocs.yml` | Config Material + `mike` (Decisión A) |
| `src/` | Symlinks al árbol canónico del repo |

Build: `mkdocs build -f mkdocs/mkdocs.yml --strict` — ver [`docs/uso-local.md`](../docs/uso-local.md).
