#!/usr/bin/env python3
"""Sync antigravity compatibility pack from a local .agent source."""
from __future__ import annotations
import argparse
import pathlib
import shutil


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, help="Path to source .agent folder")
    parser.add_argument(
        "--dest",
        default=None,
        help="Destination compatibility folder (defaults to packs/antigravity-compat/.agent)",
    )
    args = parser.parse_args()

    src = pathlib.Path(args.source).resolve()
    if not src.exists() or not src.is_dir():
        raise SystemExit(f"Invalid source: {src}")

    script_dir = pathlib.Path(__file__).resolve().parent
    skill_root = script_dir.parent
    dst = pathlib.Path(args.dest).resolve() if args.dest else skill_root / "packs" / "antigravity-compat" / ".agent"

    if dst.exists():
        shutil.rmtree(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dst)

    removed = 0
    for cache in dst.rglob("__pycache__"):
        shutil.rmtree(cache)
        removed += 1

    file_count = sum(1 for p in dst.rglob("*") if p.is_file())
    print(f"Synced pack to: {dst}")
    print(f"Files: {file_count}")
    print(f"Removed __pycache__ dirs: {removed}")


if __name__ == "__main__":
    main()
