#!/usr/bin/env python3
"""El historial publicado solo crece (sdaf-core H08 §7).

Compara la versión de la rama base con el árbol de trabajo:
- Tablas `## Historial`: las filas de la base siguen al principio, iguales y en
  el mismo orden; solo se añaden filas al final.
- CHANGELOG.md: cada sección `## [x.y.z]` de la base sigue igual.
- Un fichero con Historial en la base no desaparece salvo renombrado.

Uso: python scripts/check-history-append-only.py --base origin/main
Falla (exit 2) si no puede resolver la base: sin diff no hay garantía.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROW = re.compile(r"^\|\s*\d+\.\d+\.\d+\s*\|")


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, text=True, encoding="utf-8"
    ).stdout


def history(text: str) -> list[str] | None:
    m = re.search(r"^## Historial\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not m:
        return None
    return [ln.strip() for ln in m.group(1).splitlines() if ROW.match(ln)]


def changelog_sections(text: str) -> dict[str, str]:
    parts = re.split(r"^(## \[[^\]]+\].*)$", text, flags=re.M)
    out = {}
    for i in range(1, len(parts), 2):
        key = re.match(r"## \[([^\]]+)\]", parts[i]).group(1)
        out[key] = (parts[i] + parts[i + 1]).strip()
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--base", required=True, help="Ref de la rama base (p. ej. origin/main o un SHA)")
    args = ap.parse_args()
    try:
        base = git("rev-parse", "--verify", f"{args.base}^{{commit}}").strip()
    except subprocess.CalledProcessError:
        print(f"ERROR no se puede resolver la base {args.base!r}; sin diff no hay garantía")
        return 2

    renames: dict[str, str] = {}
    deleted: set[str] = set()
    for line in git("diff", "--name-status", "-M", base, "--").splitlines():
        cols = line.split("\t")
        if cols[0].startswith("R"):
            renames[cols[1]] = cols[2]
        elif cols[0] == "D":
            deleted.add(cols[1])

    errors: list[str] = []
    for rel in git("ls-tree", "-r", "--name-only", base).splitlines():
        if not rel.endswith(".md"):
            continue
        old = git("show", f"{base}:{rel}").replace("\r\n", "\n")
        cur_rel = renames.get(rel, rel)
        cur_path = ROOT / cur_rel
        if rel == "CHANGELOG.md":
            if not cur_path.is_file():
                errors.append("CHANGELOG.md: borrado")
                continue
            new_secs = changelog_sections(cur_path.read_text(encoding="utf-8").replace("\r\n", "\n"))
            for key, body in changelog_sections(old).items():
                if key.lower() == "unreleased":
                    continue
                if key not in new_secs:
                    errors.append(f"CHANGELOG.md: sección [{key}] borrada")
                elif new_secs[key] != body:
                    errors.append(f"CHANGELOG.md: sección [{key}] reescrita")
            continue
        old_rows = history(old)
        if old_rows is None:
            continue
        if rel in deleted or not cur_path.is_file():
            errors.append(f"{rel}: artefacto con Historial borrado")
            continue
        new_rows = history(cur_path.read_text(encoding="utf-8").replace("\r\n", "\n")) or []
        if new_rows[: len(old_rows)] != old_rows:
            for i, row in enumerate(old_rows):
                if i >= len(new_rows) or new_rows[i] != row:
                    errors.append(f"{cur_rel}: fila publicada borrada, movida o reescrita: {row}")
                    break

    for e in errors:
        print(f"ERROR {e}")
    print(f"check-history-append-only (base {args.base} = {base[:7]}): {'OK' if not errors else f'{len(errors)} errores'}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
