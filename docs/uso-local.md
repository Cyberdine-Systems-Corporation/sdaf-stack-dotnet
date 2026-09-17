# Uso local del sitio

## Requisitos

- Python 3.11+ y `pip`.

## Comandos exactos (Windows / PowerShell)

```powershell
# Desde la raíz del repo (sdaf-stack-dotnet/)
py -m venv .venv
.venv\Scripts\Activate.ps1

pip install -r requirements-docs.txt

# Servidor local con recarga en caliente -> http://127.0.0.1:8000
mkdocs serve

# Build de producción a ./site (mismo comando que corre el CI)
mkdocs build --strict
```

> [!TIP]
> `mkdocs build --strict` convierte en error cualquier warning (enlace roto, snippet inexistente, página fuera del `nav`). Ejecútalo antes de abrir PR sobre `docs/`.

## Convenciones de bloques de código

El resaltado de sintaxis (Pygments vía `pymdownx.highlight`) cubre, entre otros, YAML, PowerShell, Bash, Markdown, y — listo para cuando un consumidor incluya código real vía snippet — C#, SQL y JSON. Ejemplo ilustrativo (no es código del pack, solo valida el resaltado):

```csharp
// Ilustrativo: así se vería un endpoint Minimal API en un consumidor del pack.
app.MapPost("/api/pedidos", async (CrearPedidoRequest req, IPedidoService svc) =>
{
    var id = await svc.CrearAsync(req);
    return TypedResults.Created($"/api/pedidos/{id}", id);
});
```

```sql
-- Ilustrativo: trigger de auditoría típico en un consumidor con PostgreSQL.
CREATE TRIGGER trg_auditoria
AFTER INSERT ON pedidos
FOR EACH ROW EXECUTE FUNCTION fn_registrar_auditoria();
```

```json
{ "pedidoId": "P-0001", "estado": "creado" }
```

## Incluir contenido real sin duplicarlo

Las páginas de [Agentes](agents/index.md), [Skills](skills/index.md), [Playbooks](playbooks/index.md) y [Adopción](adoption/index.md) **no copian** el contenido de `agents/`, `skills/`, `playbooks/` o `ADOPT.md`: lo incluyen con `pymdownx.snippets` para que el sitio nunca quede desincronizado de la fuente Approved.

````markdown
```text
--8<-- "agents/frontend-agent.md:cuerpo"
```
````

(el ejemplo de arriba usa 4 comillas invertidas solo para poder mostrar la sintaxis; en el archivo real es una inclusión Markdown directa de una sección con nombre, no un bloque de código).

## Relacionado

| Destino | Por qué |
|---------|---------|
| [Inicio](index.md) | Hub del sitio |
| [.github/workflows/docs.yml](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/blob/main/.github/workflows/docs.yml) | Mismo build en CI |
