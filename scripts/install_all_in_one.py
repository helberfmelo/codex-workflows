#!/usr/bin/env python3
"""Install codex-workflows plus all companion packs with one command."""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


SKILL_PATHS = [
    "skills/codex-workflows",
    "skills/codex-backend-pack",
    "skills/codex-frontend-pack",
    "skills/codex-security-pack",
    "skills/codex-qa-pack",
    "skills/codex-node-validation-pack",
    "skills/codex-python-validation-pack",
    "skills/codex-rust-validation-pack",
]


def codex_home() -> Path:
    return Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))).resolve()


def installer_script_path(home: Path) -> Path:
    return home / "skills" / ".system" / "skill-installer" / "scripts" / "install-skill-from-github.py"


def skill_name_from_path(skill_path: str) -> str:
    return Path(skill_path).name


def select_paths_to_install(paths: list[str], dest_root: Path) -> tuple[list[str], list[str]]:
    install: list[str] = []
    skipped: list[str] = []
    for skill_path in paths:
        skill_name = skill_name_from_path(skill_path)
        if (dest_root / skill_name).exists():
            skipped.append(skill_name)
        else:
            install.append(skill_path)
    return install, skipped


def build_install_command(
    python_exec: str,
    installer_script: Path,
    repo: str,
    ref: str,
    method: str,
    paths: list[str],
    dest: Path | None = None,
) -> list[str]:
    cmd = [
        python_exec,
        str(installer_script),
        "--repo",
        repo,
        "--ref",
        ref,
        "--method",
        method,
        "--path",
        *paths,
    ]
    if dest is not None:
        cmd.extend(["--dest", str(dest)])
    return cmd


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default="helberfmelo/codex-workflows", help="GitHub repo in owner/repo format")
    parser.add_argument("--ref", default="main", help="Git ref/branch/tag to install from")
    parser.add_argument("--method", choices=["auto", "download", "git"], default="auto")
    parser.add_argument("--dest", help="Destination skills directory")
    parser.add_argument("--python-exec", default=sys.executable, help="Python executable")
    parser.add_argument("--installer-script", help="Path to install-skill-from-github.py")
    parser.add_argument("--dry-run", action="store_true", help="Print command without executing")
    args = parser.parse_args()

    home = codex_home()
    dest_root = Path(args.dest).resolve() if args.dest else (home / "skills")
    installer = (
        Path(args.installer_script).resolve()
        if args.installer_script
        else installer_script_path(home)
    )

    if not installer.exists():
        print(f"Error: installer script not found: {installer}", file=sys.stderr)
        return 1

    paths, skipped = select_paths_to_install(SKILL_PATHS, dest_root)
    if skipped:
        print("Skipping already installed skills: " + ", ".join(sorted(skipped)))

    if not paths:
        print("All codex-workflows skills are already installed.")
        return 0

    cmd = build_install_command(
        python_exec=args.python_exec,
        installer_script=installer,
        repo=args.repo,
        ref=args.ref,
        method=args.method,
        paths=paths,
        dest=Path(args.dest).resolve() if args.dest else None,
    )

    if args.dry_run:
        print("Dry run command:")
        print(" ".join(cmd))
        return 0

    proc = subprocess.run(cmd, check=False)
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
