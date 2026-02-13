#!/usr/bin/env python3
"""Ensure workflow files are kept in sync across all runtime locations."""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


def hash_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_map(root: Path) -> dict[str, str]:
    return {
        p.name: hash_file(p)
        for p in sorted(root.glob("*.md"))
        if p.is_file()
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--references", required=True, help="references/workflows directory")
    parser.add_argument("--template", required=True, help="templates/.agent/workflows directory")
    parser.add_argument("--pack", required=True, help="packs/antigravity-compat/.agent/workflows directory")
    args = parser.parse_args()

    refs = load_map(Path(args.references).resolve())
    tpl = load_map(Path(args.template).resolve())
    pack = load_map(Path(args.pack).resolve())

    names = set(refs) | set(tpl) | set(pack)
    errors: list[str] = []
    for name in sorted(names):
        if name not in refs:
            errors.append(f"missing in references: {name}")
            continue
        if name not in tpl:
            errors.append(f"missing in template: {name}")
            continue
        if name not in pack:
            errors.append(f"missing in pack: {name}")
            continue
        hashes = {refs[name], tpl[name], pack[name]}
        if len(hashes) != 1:
            errors.append(f"content mismatch: {name}")

    if errors:
        print("FAIL: workflow parity check failed")
        for item in errors:
            print(f"- {item}")
        raise SystemExit(1)

    print(f"OK: workflow parity passed ({len(names)} files)")


if __name__ == "__main__":
    main()

