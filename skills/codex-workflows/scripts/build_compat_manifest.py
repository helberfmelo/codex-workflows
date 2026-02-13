#!/usr/bin/env python3
"""Build a checksum manifest for compatibility and template trees."""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path

SKIP_EXT = {".pyc"}


def should_skip(path: Path) -> bool:
    parts = set(path.parts)
    if "__pycache__" in parts:
        return True
    if path.suffix.lower() in SKIP_EXT:
        return True
    return False


def hash_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def collect(root: Path) -> dict[str, dict[str, str | int]]:
    files: dict[str, dict[str, str | int]] = {}
    for file_path in sorted(p for p in root.rglob("*") if p.is_file()):
        rel = file_path.relative_to(root).as_posix()
        if should_skip(Path(rel)):
            continue
        files[rel] = {
            "sha256": hash_file(file_path),
            "size": file_path.stat().st_size,
        }
    return files


def digest_map(files: dict[str, dict[str, str | int]]) -> str:
    h = hashlib.sha256()
    for rel in sorted(files):
        h.update(rel.encode("utf-8"))
        h.update(str(files[rel]["sha256"]).encode("utf-8"))
        h.update(str(files[rel]["size"]).encode("utf-8"))
    return h.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, help="Source .agent directory")
    parser.add_argument("--pack", required=True, help="Compatibility pack .agent directory")
    parser.add_argument("--template-full", required=True, help="Full template .agent directory")
    parser.add_argument("--output", required=True, help="Output JSON manifest path")
    args = parser.parse_args()

    source = Path(args.source).resolve()
    pack = Path(args.pack).resolve()
    template_full = Path(args.template_full).resolve()
    output = Path(args.output).resolve()

    data = {
        "generated_at_utc": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": {"path": args.source, "files": collect(source)},
        "pack": {"path": args.pack, "files": collect(pack)},
        "template_full": {"path": args.template_full, "files": collect(template_full)},
    }
    for key in ("source", "pack", "template_full"):
        files = data[key]["files"]
        data[key]["count"] = len(files)
        data[key]["digest_sha256"] = digest_map(files)

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(f"Manifest written: {output}")
    print(f"source={data['source']['count']} pack={data['pack']['count']} template_full={data['template_full']['count']}")


if __name__ == "__main__":
    main()
