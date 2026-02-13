#!/usr/bin/env python3
"""Bootstrap a local .agent folder from bundled profiles."""
from __future__ import annotations
import argparse
import pathlib
import shutil


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", default=".", help="Project root path")
    parser.add_argument(
        "--profile",
        default="antigravity-compat",
        choices=("minimal", "antigravity-compat"),
        help="Template profile to install",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing .agent files")
    args = parser.parse_args()

    skill_root = pathlib.Path(__file__).resolve().parents[1]
    if args.profile == "minimal":
        src = skill_root / "templates" / ".agent"
    else:
        src = skill_root / "packs" / "antigravity-compat" / ".agent"
    dst = pathlib.Path(args.project).resolve() / ".agent"

    if dst.exists() and not args.force:
        raise SystemExit(".agent already exists. Use --force to overwrite.")

    if dst.exists() and args.force:
        shutil.rmtree(dst)

    shutil.copytree(src, dst)
    print(f"Bootstrapped profile '{args.profile}' at: {dst}")


if __name__ == "__main__":
    main()
