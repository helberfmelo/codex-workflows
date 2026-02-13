#!/usr/bin/env python3
"""Bootstrap a local .agent folder from bundled templates."""
from __future__ import annotations
import argparse
import pathlib
import shutil


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", default=".", help="Project root path")
    parser.add_argument("--force", action="store_true", help="Overwrite existing .agent files")
    args = parser.parse_args()

    skill_root = pathlib.Path(__file__).resolve().parents[1]
    src = skill_root / "templates" / ".agent"
    dst = pathlib.Path(args.project).resolve() / ".agent"

    if dst.exists() and not args.force:
        raise SystemExit(".agent already exists. Use --force to overwrite.")

    if dst.exists() and args.force:
        shutil.rmtree(dst)

    shutil.copytree(src, dst)
    print(f"Bootstrapped: {dst}")


if __name__ == "__main__":
    main()
