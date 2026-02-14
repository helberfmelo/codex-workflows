#!/usr/bin/env python3
"""Unified CLI for codex-workflows operations."""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "skills" / "codex-workflows"
WEBSITE_ROOT = REPO_ROOT / "website"


def run_command(cmd: list[str], *, cwd: Path | None = None) -> int:
    proc = subprocess.run(cmd, cwd=str(cwd) if cwd else None, check=False)
    return proc.returncode


def npm_executable() -> str:
    direct = shutil.which("npm")
    if direct:
        return direct
    if os.name == "nt":
        npm_cmd = shutil.which("npm.cmd")
        if npm_cmd:
            return npm_cmd
    raise SystemExit("npm executable not found in PATH.")


def git_value(args: list[str]) -> str:
    proc = subprocess.run(
        ["git", "-C", str(REPO_ROOT), *args],
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if proc.returncode != 0:
        return "unknown"
    return proc.stdout.strip() or "unknown"


def locale_parity_counts(docs_root: Path) -> dict[str, object]:
    locales = {"pt", "es", "fr", "zh"}
    exclude = {".vitepress", "public"}
    all_rel = [p.relative_to(docs_root) for p in docs_root.rglob("*.md")]
    en_files = sorted(
        ["/".join(p.parts) for p in all_rel if p.parts[0] not in locales and p.parts[0] not in exclude]
    )
    base = set(en_files)
    locale_report: dict[str, object] = {}
    for lang in sorted(locales):
        lang_root = docs_root / lang
        lang_files = (
            sorted(["/".join(p.relative_to(lang_root).parts) for p in lang_root.rglob("*.md")])
            if lang_root.exists()
            else []
        )
        missing = sorted(base - set(lang_files))
        locale_report[lang] = {
            "count": len(lang_files),
            "missing": len(missing),
            "missing_examples": missing[:5],
        }
    return {"en_count": len(base), "locales": locale_report}


def cmd_install(args: argparse.Namespace) -> int:
    cmd = [sys.executable, str(REPO_ROOT / "scripts" / "install_all_in_one.py")]
    if args.repo:
        cmd.extend(["--repo", args.repo])
    if args.ref:
        cmd.extend(["--ref", args.ref])
    if args.method:
        cmd.extend(["--method", args.method])
    if args.dest:
        cmd.extend(["--dest", args.dest])
    if args.python_exec:
        cmd.extend(["--python-exec", args.python_exec])
    if args.installer_script:
        cmd.extend(["--installer-script", args.installer_script])
    if args.dry_run:
        cmd.append("--dry-run")
    return run_command(cmd, cwd=REPO_ROOT)


def cmd_init(args: argparse.Namespace) -> int:
    cmd = [
        sys.executable,
        str(SKILL_ROOT / "scripts" / "bootstrap_project_agent.py"),
        "--project",
        args.project,
        "--profile",
        args.profile,
    ]
    if args.force:
        cmd.append("--force")
    return run_command(cmd, cwd=REPO_ROOT)


def cmd_docs_sync(args: argparse.Namespace) -> int:
    sync_cmd = [sys.executable, str(WEBSITE_ROOT / "scripts" / "sync_reference_docs.py")]
    code = run_command(sync_cmd, cwd=REPO_ROOT)
    if code != 0:
        return code
    if args.build:
        return run_command([npm_executable(), "run", "docs:build"], cwd=WEBSITE_ROOT)
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    commands: list[tuple[list[str], Path | None]] = [
        (
            [
                sys.executable,
                str(SKILL_ROOT / "scripts" / "check_workflow_parity.py"),
                "--references",
                str(SKILL_ROOT / "references" / "workflows"),
                "--native",
                str(SKILL_ROOT / "templates" / "codex-native" / ".agent" / "workflows"),
                "--template",
                str(SKILL_ROOT / "templates" / ".agent" / "workflows"),
                "--pack",
                str(SKILL_ROOT / "packs" / "antigravity-compat" / ".agent" / "workflows"),
            ],
            REPO_ROOT,
        ),
        (
            [
                sys.executable,
                str(SKILL_ROOT / "scripts" / "check_codex_native_quality.py"),
                "--native",
                str(SKILL_ROOT / "templates" / "codex-native" / ".agent" / "workflows"),
                "--compat",
                str(SKILL_ROOT / "packs" / "antigravity-compat" / ".agent" / "workflows"),
                "--max-similarity",
                "0.35",
            ],
            REPO_ROOT,
        ),
        (
            [
                sys.executable,
                str(SKILL_ROOT / "scripts" / "check_codex_native_assets.py"),
                "--native-root",
                str(SKILL_ROOT / "templates" / "codex-native" / ".agent"),
                "--min-agents",
                "20",
                "--min-skills",
                "37",
            ],
            REPO_ROOT,
        ),
        (
            [
                sys.executable,
                str(SKILL_ROOT / "scripts" / "check_codex_native_rules.py"),
                "--native-root",
                str(SKILL_ROOT / "templates" / "codex-native" / ".agent"),
            ],
            REPO_ROOT,
        ),
    ]
    if args.tests:
        commands.append(([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"], REPO_ROOT))
    if args.docs:
        commands.append(([sys.executable, str(WEBSITE_ROOT / "scripts" / "sync_reference_docs.py")], REPO_ROOT))
        commands.append(([npm_executable(), "run", "docs:build"], WEBSITE_ROOT))

    for cmd, cwd in commands:
        code = run_command(cmd, cwd=cwd)
        if code != 0:
            return code
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    data = {
        "repo": str(REPO_ROOT),
        "git_branch": git_value(["rev-parse", "--abbrev-ref", "HEAD"]),
        "git_commit": git_value(["rev-parse", "HEAD"]),
        "codex_native_workflows": len(list((SKILL_ROOT / "templates" / "codex-native" / ".agent" / "workflows").glob("*.md"))),
        "codex_native_agents": len(list((SKILL_ROOT / "templates" / "codex-native" / ".agent" / "agents").glob("*.md"))),
        "codex_native_skills": len([p for p in (SKILL_ROOT / "templates" / "codex-native" / ".agent" / "skills").iterdir() if p.is_dir()]),
        "codex_native_global_rules": len(list((SKILL_ROOT / "templates" / "codex-native" / ".agent" / "rules" / "global").glob("*.md"))),
        "codex_native_domain_rules": len(list((SKILL_ROOT / "templates" / "codex-native" / ".agent" / "rules" / "domains").glob("*.md"))),
        "codex_native_workflow_rules": len(list((SKILL_ROOT / "templates" / "codex-native" / ".agent" / "rules" / "workflows").glob("*.md"))),
        "compat_workflows": len(list((SKILL_ROOT / "packs" / "antigravity-compat" / ".agent" / "workflows").glob("*.md"))),
        "docs_locale_parity": locale_parity_counts(WEBSITE_ROOT / "docs"),
    }
    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print("codexwf status")
        print(f"- branch: {data['git_branch']}")
        print(f"- commit: {data['git_commit']}")
        print(f"- codex-native workflows: {data['codex_native_workflows']}")
        print(f"- codex-native agents: {data['codex_native_agents']}")
        print(f"- codex-native skills: {data['codex_native_skills']}")
        print(
            "- codex-native rules: "
            f"global={data['codex_native_global_rules']} "
            f"domains={data['codex_native_domain_rules']} "
            f"workflows={data['codex_native_workflow_rules']}"
        )
        print(f"- compat workflows: {data['compat_workflows']}")
        parity = data["docs_locale_parity"]
        print(f"- docs EN pages: {parity['en_count']}")
        for lang, item in parity["locales"].items():
            print(f"  - {lang}: count={item['count']} missing={item['missing']}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Unified CLI for codex-workflows operations.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_install = sub.add_parser("install", help="Install all codex-workflows packs.")
    p_install.add_argument("--repo", default="helberfmelo/codex-workflows")
    p_install.add_argument("--ref", default="main")
    p_install.add_argument("--method", choices=["auto", "download", "git"], default="auto")
    p_install.add_argument("--dest")
    p_install.add_argument("--python-exec")
    p_install.add_argument("--installer-script")
    p_install.add_argument("--dry-run", action="store_true")
    p_install.set_defaults(func=cmd_install)

    p_init = sub.add_parser("init", help="Bootstrap local .agent profile.")
    p_init.add_argument("--project", default=".")
    p_init.add_argument("--profile", choices=["codex-native", "minimal", "antigravity-compat"], default="codex-native")
    p_init.add_argument("--force", action="store_true")
    p_init.set_defaults(func=cmd_init)

    p_validate = sub.add_parser("validate", help="Run core repository validations.")
    p_validate.add_argument("--tests", action="store_true", help="Include unit tests.")
    p_validate.add_argument("--docs", action="store_true", help="Include docs sync and docs build.")
    p_validate.set_defaults(func=cmd_validate)

    p_status = sub.add_parser("status", help="Show repository status snapshot.")
    p_status.add_argument("--json", action="store_true")
    p_status.set_defaults(func=cmd_status)

    p_docs = sub.add_parser("docs-sync", help="Sync website source docs.")
    p_docs.add_argument("--build", action="store_true", help="Also build docs after syncing.")
    p_docs.set_defaults(func=cmd_docs_sync)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

