#!/usr/bin/env python3
"""Bootstrap a local .agent folder from bundled profiles."""
from __future__ import annotations
import argparse
import pathlib
import shutil


PROFILE_CHOICES = ("codex-native", "minimal", "antigravity-compat")


def profile_sources(skill_root: pathlib.Path, profile: str) -> list[pathlib.Path]:
    if profile == "minimal":
        return [skill_root / "templates" / "minimal" / ".agent"]
    if profile == "antigravity-compat":
        return [skill_root / "packs" / "antigravity-compat" / ".agent"]
    if profile == "codex-native":
        return [
            skill_root / "packs" / "antigravity-compat" / ".agent",
            skill_root / "templates" / "codex-native" / ".agent",
        ]
    raise ValueError(f"Unsupported profile: {profile}")


def copy_profile_sources(sources: list[pathlib.Path], destination: pathlib.Path) -> None:
    for idx, src in enumerate(sources):
        if not src.exists():
            raise SystemExit(f"Profile source not found: {src}")
        if idx == 0:
            shutil.copytree(src, destination)
        else:
            shutil.copytree(src, destination, dirs_exist_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", default=".", help="Project root path")
    parser.add_argument(
        "--profile",
        default="codex-native",
        choices=PROFILE_CHOICES,
        help="Template profile to install",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing .agent files")
    args = parser.parse_args()

    skill_root = pathlib.Path(__file__).resolve().parents[1]
    sources = profile_sources(skill_root, args.profile)
    dst = pathlib.Path(args.project).resolve() / ".agent"

    if dst.exists() and not args.force:
        raise SystemExit(".agent already exists. Use --force to overwrite.")

    if dst.exists() and args.force:
        shutil.rmtree(dst)

    copy_profile_sources(sources, dst)
    print(f"Bootstrapped profile '{args.profile}' at: {dst}")


if __name__ == "__main__":
    main()
