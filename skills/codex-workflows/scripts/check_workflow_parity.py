#!/usr/bin/env python3
"""Validate split workflow contracts for native and compatibility tracks."""
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


def check_pair(label_a: str, map_a: dict[str, str], label_b: str, map_b: dict[str, str]) -> list[str]:
    errors: list[str] = []
    names = set(map_a) | set(map_b)
    for name in sorted(names):
        if name not in map_a:
            errors.append(f"missing in {label_a}: {name}")
            continue
        if name not in map_b:
            errors.append(f"missing in {label_b}: {name}")
            continue
        if map_a[name] != map_b[name]:
            errors.append(f"content mismatch between {label_a} and {label_b}: {name}")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--references", required=True, help="references/workflows directory")
    parser.add_argument("--native", help="templates/codex-native/.agent/workflows directory")
    parser.add_argument("--template", required=True, help="templates/.agent/workflows (compat template) directory")
    parser.add_argument("--pack", required=True, help="packs/antigravity-compat/.agent/workflows directory")
    args = parser.parse_args()

    script_root = Path(__file__).resolve().parents[1]
    refs = load_map(Path(args.references).resolve())
    native_dir = Path(args.native).resolve() if args.native else script_root / "templates" / "codex-native" / ".agent" / "workflows"
    native = load_map(native_dir)
    tpl = load_map(Path(args.template).resolve())
    pack = load_map(Path(args.pack).resolve())

    errors = []
    errors.extend(check_pair("references", refs, "native", native))
    errors.extend(check_pair("compat-template", tpl, "compat-pack", pack))

    if errors:
        print("FAIL: workflow parity check failed")
        for item in errors:
            print(f"- {item}")
        raise SystemExit(1)

    print(
        "OK: workflow parity passed "
        f"(native={len(set(refs) | set(native))} files, compat={len(set(tpl) | set(pack))} files)"
    )


if __name__ == "__main__":
    main()
