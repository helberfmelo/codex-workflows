#!/usr/bin/env python3
"""Check compatibility pack/template drift against a manifest."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from build_compat_manifest import collect, digest_map


def compare_bucket(name: str, expected: dict, actual_path: Path) -> list[str]:
    errors: list[str] = []
    expected_files = expected["files"]
    actual_files = collect(actual_path)
    if set(expected_files) != set(actual_files):
        missing = sorted(set(expected_files) - set(actual_files))
        extra = sorted(set(actual_files) - set(expected_files))
        if missing:
            errors.append(f"[{name}] missing files: {len(missing)}")
            errors.extend([f"  - {m}" for m in missing[:20]])
        if extra:
            errors.append(f"[{name}] unexpected files: {len(extra)}")
            errors.extend([f"  + {e}" for e in extra[:20]])
    changed = []
    for rel in sorted(set(expected_files) & set(actual_files)):
        if expected_files[rel]["sha256"] != actual_files[rel]["sha256"]:
            changed.append(rel)
    if changed:
        errors.append(f"[{name}] checksum mismatches: {len(changed)}")
        errors.extend([f"  * {c}" for c in changed[:20]])
    if expected.get("digest_sha256") != digest_map(actual_files):
        errors.append(f"[{name}] digest_sha256 differs from manifest")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True, help="Manifest JSON file")
    parser.add_argument("--pack", required=True, help="Compatibility pack .agent directory")
    parser.add_argument("--template-full", required=True, help="Full template .agent directory")
    parser.add_argument("--source", help="Optional source .agent directory to verify against source bucket")
    args = parser.parse_args()

    manifest = Path(args.manifest).resolve()
    data = json.loads(manifest.read_text(encoding="utf-8"))

    errors: list[str] = []
    errors += compare_bucket("pack", data["pack"], Path(args.pack).resolve())
    errors += compare_bucket("template_full", data["template_full"], Path(args.template_full).resolve())
    if args.source:
        errors += compare_bucket("source", data["source"], Path(args.source).resolve())

    if errors:
        print("FAIL: compatibility drift detected")
        for e in errors:
            print(e)
        raise SystemExit(1)
    print("OK: compatibility drift check passed")


if __name__ == "__main__":
    main()

