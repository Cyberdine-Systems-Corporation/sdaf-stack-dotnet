#!/usr/bin/env python3
"""Coherencia del pack contra pack.yaml (fuente de verdad de versión y compat).

Comprueba:
- pack.yaml: id, semver, rango sdaf_core; rutas de agentes, prompts, skills y
  playbooks del manifest (y que no haya skills ni contratos sin declarar).
- Cabeceras de contratos, prompts, skills y playbooks: `Pack` = id@version,
  `Versión` = version del pack, `Fecha` = fecha de la fila más reciente de la
  versión máxima del Historial (sdaf-core H13 §9).
- Historial: versiones crecientes; fechas ISO 8601; desde HORA_DESDE, fila con
  hora y zona (AAAA-MM-DDThh:mm±hh:mm).
- Citas `sdaf-stack-dotnet@x.y.z` y `<skill>@x.y.z` fuera de historiales y del
  CHANGELOG = versión vigente.
- examples/*.yaml: stack.pack = id@version y sdaf.version dentro de sdaf_core.
- README (Id y Compat), CHANGELOG (entrada de la versión) y ADRs del pack
  (numeración desde 001, estado, fila en el índice).

Uso: python scripts/check-pack-metadata.py [--root RUTA]
Exit 1 si hay algún error.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

HORA_DESDE = (0, 3, 0)
SEMVER = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")
DAY = r"\d{4}-\d{2}-\d{2}"
DATETIME = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2})?(?:Z|[+-]\d{2}:\d{2})"
DATE_ANY = re.compile(rf"^(?:{DATETIME}|{DAY})$")
DATE_TIME = re.compile(rf"^{DATETIME}$")
RANGE = re.compile(r"^>=(\d+\.\d+\.\d+) <(\d+\.\d+\.\d+)$")
ROW = re.compile(r"^\|\s*(\d+\.\d+\.\d+)\s*\|\s*([^|]+?)\s*\|")
ADR_FILE = re.compile(r"^ADR-(\d{3})-[a-z0-9-]+\.md$")
ADR_ESTADOS = {"Propuesto", "Aceptado", "Derogado"}
SKIP_DIRS = {".git", ".venv", "venv", "site", "node_modules", "worklogs", ".sdaf-core"}


def ver(s: str) -> tuple[int, int, int]:
    m = SEMVER.match(s)
    if not m:
        raise ValueError(s)
    return tuple(int(x) for x in m.groups())  # type: ignore[return-value]


def header_fields(text: str) -> dict[str, str]:
    """Primera tabla `| Campo | Valor |` del documento."""
    fields: dict[str, str] = {}
    in_table = False
    for line in text.splitlines():
        if re.match(r"^\|\s*Campo\s*\|\s*Valor\s*\|", line):
            in_table = True
            continue
        if in_table:
            if not line.startswith("|"):
                break
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 2 and not set(cells[0]) <= {"-", " "}:
                fields[cells[0]] = cells[1].strip("`")
    return fields


def section(text: str, title: str) -> str | None:
    m = re.search(rf"^## {re.escape(title)}\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else None


def history_rows(text: str) -> list[tuple[str, str]] | None:
    body = section(text, "Historial")
    if body is None:
        return None
    return [(m.group(1), m.group(2)) for m in map(ROW.match, body.splitlines()) if m]


def frontmatter(text: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return yaml.safe_load(m.group(1)) if m else {}


def strip_history(text: str) -> str:
    return re.sub(r"^## Historial\s*$.*?(?=^## |\Z)", "", text, flags=re.M | re.S)


def check(root: Path) -> list[str]:
    errors: list[str] = []

    def err(where: str, msg: str) -> None:
        errors.append(f"{where}: {msg}")

    def read(rel: str) -> str:
        return (root / rel).read_text(encoding="utf-8").replace("\r\n", "\n")

    # --- pack.yaml -----------------------------------------------------------
    pack = yaml.safe_load(read("pack.yaml"))
    pid, pver, compat = pack.get("id"), str(pack.get("version", "")), str(pack.get("sdaf_core", ""))
    if pid != "sdaf-stack-dotnet":
        err("pack.yaml", f"id inesperado: {pid!r}")
    if not SEMVER.match(pver):
        err("pack.yaml", f"version no es semver: {pver!r}")
        return errors
    rng = RANGE.match(compat)
    if not rng:
        err("pack.yaml", f"sdaf_core no tiene la forma '>=X.Y.Z <X.Y.Z': {compat!r}")
    ident = f"{pid}@{pver}"

    agents = list(pack.get("agents", {}).get("extension", []) or [])
    skills: dict[str, str] = {}
    for s in pack.get("skills", []) or []:
        sid, _, sver = str(s).partition("@")
        skills[sid] = sver
        if sver != pver:
            err("pack.yaml", f"skill {s}: la versión debe ser la del pack ({pver})")
    playbooks = list(pack.get("playbooks", []) or [])

    versioned: list[str] = []
    for a in agents:
        for rel in (f"agents/{a}-agent.md", f"prompts/agents/{a}-agent.md"):
            if (root / rel).is_file():
                versioned.append(rel)
            else:
                err("pack.yaml", f"agente {a}: falta {rel}")
    for sid in skills:
        rel = f"skills/{sid}/SKILL.md"
        if not (root / rel).is_file():
            err("pack.yaml", f"skill {sid}: falta {rel}")
            continue
        versioned.append(rel)
        text = read(rel)
        if frontmatter(text).get("name") != sid:
            err(rel, f"frontmatter name distinto de {sid}")
        if header_fields(text).get("ID") != sid:
            err(rel, f"cabecera ID distinta de {sid}")
    for rel in playbooks:
        if (root / rel).is_file():
            versioned.append(rel)
        else:
            err("pack.yaml", f"playbook inexistente: {rel}")

    declared_agents = {f"agents/{a}-agent.md" for a in agents}
    for p in sorted((root / "agents").glob("*-agent.md")):
        rel = p.relative_to(root).as_posix()
        if rel not in declared_agents:
            err(rel, "contrato no declarado en pack.yaml (agents.extension)")
    for p in sorted((root / "skills").glob("*/SKILL.md")):
        if p.parent.name not in skills:
            err(p.relative_to(root).as_posix(), "skill no declarada en pack.yaml")

    # --- cabeceras e historial ----------------------------------------------
    for rel in versioned:
        text = read(rel)
        h = header_fields(text)
        if h.get("Pack") != ident:
            err(rel, f"Pack = {h.get('Pack')!r}; esperado {ident!r}")
        if h.get("Versión") != pver:
            err(rel, f"Versión = {h.get('Versión')!r}; esperado {pver!r} (release alinea todos los artefactos)")
        rows = history_rows(text)
        if not rows:
            err(rel, "sin sección Historial con filas | versión | fecha | cambio |")
            continue
        prev = None
        for v, d in rows:
            if not DATE_ANY.match(d):
                err(rel, f"Historial {v}: fecha {d!r} no es ISO 8601")
            elif ver(v) >= HORA_DESDE and not DATE_TIME.match(d):
                err(rel, f"Historial {v}: desde {'.'.join(map(str, HORA_DESDE))} la fecha lleva hora y zona ({d!r})")
            if prev is not None and ver(v) < ver(prev):
                err(rel, f"Historial: {v} después de {prev} (versiones no crecientes)")
            prev = v
        top = max(rows, key=lambda r: ver(r[0]))[0]
        if top != h.get("Versión"):
            err(rel, f"Versión de cabecera {h.get('Versión')!r} ≠ versión máxima del Historial {top!r}")
        latest = [d for v, d in rows if v == top][-1]
        if h.get("Fecha") != latest:
            err(rel, f"Fecha de cabecera {h.get('Fecha')!r} ≠ fila más reciente de {top} ({latest!r})")

    # --- citas id@version ----------------------------------------------------
    cite = re.compile(rf"\b({re.escape(pid)}|{'|'.join(map(re.escape, skills))})@(\d+\.\d+\.\d+)\b")
    for p in sorted(root.rglob("*")):
        if p.suffix not in {".md", ".yaml", ".yml", ".mdc"} or not p.is_file():
            continue
        parts = p.relative_to(root).parts
        if set(parts[:-1]) & SKIP_DIRS or parts[0] == "scripts":
            continue
        rel = p.relative_to(root).as_posix()
        if rel == "CHANGELOG.md":
            continue
        body = strip_history(read(rel))
        for n, line in enumerate(body.splitlines(), 1):
            for m in cite.finditer(line):
                want = pver if m.group(1) == pid else skills[m.group(1)]
                if m.group(2) != want:
                    err(rel, f"cita {m.group(0)} (vigente: {m.group(1)}@{want})")

    # --- examples ------------------------------------------------------------
    for p in sorted((root / "examples").glob("*.yaml")):
        rel = p.relative_to(root).as_posix()
        cfg = yaml.safe_load(read(rel)) or {}
        if (cfg.get("stack") or {}).get("pack") != ident:
            err(rel, f"stack.pack = {(cfg.get('stack') or {}).get('pack')!r}; esperado {ident!r}")
        sv = str((cfg.get("sdaf") or {}).get("version", ""))
        if rng and SEMVER.match(sv):
            if not (ver(rng.group(1)) <= ver(sv) < ver(rng.group(2))):
                err(rel, f"sdaf.version {sv} fuera de sdaf_core {compat}")
        elif rng:
            err(rel, f"sdaf.version no es semver: {sv!r}")

    # --- README y CHANGELOG --------------------------------------------------
    rh = header_fields(read("README.md"))
    if rh.get("Id") != ident:
        err("README.md", f"Id = {rh.get('Id')!r}; esperado {ident!r}")
    if compat not in read("README.md"):
        err("README.md", f"no cita el rango de compat {compat!r}")
    if not re.search(rf"^## \[{re.escape(pver)}\]", read("CHANGELOG.md"), re.M):
        err("CHANGELOG.md", f"sin entrada '## [{pver}]'")

    # --- ADRs del pack -------------------------------------------------------
    adr_dir = root / "docs/architecture/adr"
    index = read("docs/architecture/adr/index.md") if (adr_dir / "index.md").is_file() else ""
    nums = []
    for p in sorted(adr_dir.glob("*.md")):
        if p.name in {"index.md", "plantilla-adr.md"}:
            continue
        rel = p.relative_to(root).as_posix()
        m = ADR_FILE.match(p.name)
        if not m:
            err(rel, "nombre de ADR fuera del formato ADR-NNN-slug.md")
            continue
        nums.append(int(m.group(1)))
        text = read(rel)
        if not text.startswith(f"# ADR-{m.group(1)} "):
            err(rel, f"el título no empieza por 'ADR-{m.group(1)}'")
        estado = header_fields(text).get("Estado")
        if estado not in ADR_ESTADOS:
            err(rel, f"Estado {estado!r} fuera de {sorted(ADR_ESTADOS)}")
        if f"]({p.name})" not in index:
            err("docs/architecture/adr/index.md", f"no enlaza {p.name}")
    if nums and sorted(nums) != list(range(1, len(nums) + 1)):
        err("docs/architecture/adr", f"numeración no contigua desde 001: {sorted(nums)}")

    return errors


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = ap.parse_args()
    errors = check(args.root)
    for e in errors:
        print(f"ERROR {e}")
    print(f"check-pack-metadata: {'OK' if not errors else f'{len(errors)} errores'}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
