#!/usr/bin/env python3
"""Autocomprobación de check-pack-metadata.py.

Copia el repo a un directorio temporal, comprueba que pasa y aplica mutaciones
que deben fallar (una por caso). Exit 1 si el checker acepta una mutación o
rechaza el árbol real.
"""
from __future__ import annotations

import importlib.util
import re
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("cpm", ROOT / "scripts" / "check-pack-metadata.py")
cpm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cpm)  # type: ignore[union-attr]

IGNORE = shutil.ignore_patterns(".git", ".venv", "venv", "site", ".sdaf-core", "__pycache__")


def sub(rel: str, pattern: str, repl: str):
    def apply(root: Path) -> None:
        p = root / rel
        text = p.read_text(encoding="utf-8")
        new, n = re.subn(pattern, repl, text, count=1, flags=re.M)
        assert n == 1, f"la mutación no aplica: {rel} {pattern!r}"
        p.write_text(new, encoding="utf-8")
    return apply


def append(rel: str, extra: str):
    def apply(root: Path) -> None:
        p = root / rel
        p.write_text(p.read_text(encoding="utf-8") + extra, encoding="utf-8")
    return apply


def delete(rel: str):
    return lambda root: (root / rel).unlink()


CASES = {
    "version del pack sin propagar": sub("pack.yaml", r'^version: "[^"]+"', 'version: "9.9.9"'),
    "sdaf_core mal formado": sub("pack.yaml", r"^sdaf_core: .*$", 'sdaf_core: "0.4.x"'),
    "Versión de skill desalineada": sub("skills/aspire-local-run/SKILL.md", r"^\| Versión \| [^|]+\|", "| Versión | 0.2.9 |"),
    "Pack de contrato desalineado": sub("agents/frontend-agent.md", r"^\| Pack \| [^|]+\|", "| Pack | sdaf-stack-dotnet@0.2.0 |"),
    "Fecha de cabecera ≠ última fila": sub("playbooks/vertical-slice-cqrs.md", r"^\| Fecha \| [^|]+\|", "| Fecha | 2026-01-01T00:00+02:00 |"),
    "fila nueva sin hora": sub("prompts/agents/frontend-agent.md", r"^(\| 0\.3\.0 \| )[^|]+\|", r"\g<1>2026-09-25 |"),
    "Historial no creciente": sub("agents/infrastructure-agent.md", r"^\| 0\.1\.1 \|", "| 0.0.9 |"),
    "contrato sin Historial": sub("agents/domain-application-agent.md", r"^## Historial$", "## Versiones"),
    "cita skill@version vieja": append("docs/uso-local.md", "\nUsa `csharp-adr006-slice@0.2.0`.\n"),
    "cita pack@version vieja": append("skills/README.md", "\nVer `sdaf-stack-dotnet@0.1.1`.\n"),
    "examples con stack.pack viejo": sub("examples/01-pack-only.yaml", r"pack: sdaf-stack-dotnet@\S+", "pack: sdaf-stack-dotnet@0.2.0"),
    "examples con sdaf.version fuera de compat": sub("examples/02-pack-frontend.yaml", r'version: "[^"]+"', 'version: "0.3.0"'),
    "skill sin declarar": lambda root: shutil.copytree(root / "skills/aspire-local-run", root / "skills/aspire-extra"),
    "playbook del manifest inexistente": delete("playbooks/vertical-slice-cqrs.md"),
    "frontmatter name de skill distinto": sub("skills/blazor-bff-slice/SKILL.md", r"^name: .*$", "name: blazor-otro"),
    "README con Id viejo": sub("README.md", r"^\| Id \| [^|]+\|", "| Id | `sdaf-stack-dotnet@0.2.0` |"),
    "CHANGELOG sin entrada": sub("CHANGELOG.md", r"^## \[0\.3\.0\]", "## [0.3.0-borrador]"),
    "ADR fuera del índice": sub("docs/architecture/adr/index.md", r"\]\(ADR-002-infrastructure-stub\.md\)", "](x.md)"),
    "ADR con estado inválido": sub("docs/architecture/adr/ADR-001-fusion-domain-application.md", r"^\| Estado \| [^|]+\|", "| Estado | Approved |"),
    "ADR con numeración con hueco": lambda root: (root / "docs/architecture/adr/ADR-002-infrastructure-stub.md").rename(
        root / "docs/architecture/adr/ADR-003-infrastructure-stub.md"),
}


def main() -> int:
    failures = 0
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp) / "base"
        shutil.copytree(ROOT, base, ignore=IGNORE)
        errs = cpm.check(base)
        if errs:
            print("FALLO el árbol real no pasa:", *errs, sep="\n  ")
            return 1
        print("OK   árbol real")
        for i, (name, mutate) in enumerate(CASES.items()):
            case = Path(tmp) / f"c{i}"
            shutil.copytree(base, case)
            mutate(case)
            errs = cpm.check(case)
            if errs:
                print(f"OK   {name}: {errs[0]}")
            else:
                print(f"FALLO {name}: el checker la aceptó")
                failures += 1
    print(f"test-check-pack-metadata: {len(CASES) - failures}/{len(CASES)} mutaciones detectadas")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
