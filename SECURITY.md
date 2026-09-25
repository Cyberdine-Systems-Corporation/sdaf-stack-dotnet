# Seguridad — aviso de este repositorio

Canal de aviso para vulnerabilidades de **sdaf-stack-dotnet** (este repo): [aviso privado de GitHub](https://github.com/Cyberdine-Systems-Corporation/sdaf-stack-dotnet/security/advisories/new). No abras un issue público.

El pack no contiene código ejecutable de producto: su superficie son los workflows de CI, los scripts de `scripts/` y lo que contratos, skills y prompts instruyen a un agente (por ejemplo, una instrucción que relaje Gate 0, autorice escritura al remoto o pida secretos).

Las correcciones se publican sobre la última versión del pack. Si una corrección se lleva a versiones anteriores lo decide la identidad de [`CODEOWNERS`](CODEOWNERS).

Este fichero es la política de aviso del pack. La plantilla de reporte que el consumidor materializa en su propio `SECURITY.md` vive en sdaf-core (`templates/security.md`, H12).

## Relacionado

| | Destino | Por qué |
|--|---------|---------|
| 🧭 | [README.md](README.md) | Hub del pack |
| 🛠️ | [CONTRIBUTING.md](CONTRIBUTING.md) | Flujo de cambios |
