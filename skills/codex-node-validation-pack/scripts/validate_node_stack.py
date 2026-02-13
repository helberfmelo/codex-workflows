#!/usr/bin/env python3
"""Validate Node.js/TypeScript projects with script-aware checks."""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


LOCKFILE_TO_MANAGER = (
    ("pnpm-lock.yaml", "pnpm"),
    ("yarn.lock", "yarn"),
    ("bun.lockb", "bun"),
    ("package-lock.json", "npm"),
    ("npm-shrinkwrap.json", "npm"),
)


def _load_package_json(path: Path) -> dict:
    pkg = path / "package.json"
    if not pkg.exists():
        raise SystemExit(f"package.json not found under: {path}")
    return json.loads(pkg.read_text(encoding="utf-8"))


def detect_package_manager(project: Path) -> str:
    for lockfile, manager in LOCKFILE_TO_MANAGER:
        if (project / lockfile).exists():
            return manager
    return "npm"


def script_command(manager: str, script: str) -> str:
    if manager == "npm":
        return "npm test" if script == "test" else f"npm run {script}"
    if manager == "yarn":
        return f"yarn {script}"
    if manager == "pnpm":
        return f"pnpm {script}" if script == "test" else f"pnpm run {script}"
    if manager == "bun":
        return "bun test" if script == "test" else f"bun run {script}"
    raise ValueError(f"unsupported manager: {manager}")


def build_checks(project: Path) -> list[str]:
    pkg = _load_package_json(project)
    scripts = pkg.get("scripts", {})
    manager = detect_package_manager(project)
    checks: list[str] = []

    for script in ("lint", "typecheck", "test", "build"):
        if script in scripts:
            checks.append(script_command(manager, script))

    if manager == "npm" and ((project / "package-lock.json").exists() or (project / "npm-shrinkwrap.json").exists()):
        checks.append("npm audit --audit-level=high")
    elif manager == "pnpm" and (project / "pnpm-lock.yaml").exists():
        checks.append("pnpm audit --prod")
    elif manager == "yarn" and (project / "yarn.lock").exists():
        checks.append("yarn npm audit --all")

    if not checks:
        checks = [script_command(manager, "test"), script_command(manager, "build")]

    return list(dict.fromkeys(checks))


def run_checks(project: Path, checks: list[str]) -> list[dict[str, str | int]]:
    results: list[dict[str, str | int]] = []
    for cmd in checks:
        proc = subprocess.run(cmd, cwd=project, shell=True, check=False, capture_output=True, text=True)
        results.append(
            {
                "command": cmd,
                "code": proc.returncode,
                "stdout": proc.stdout[-4000:],
                "stderr": proc.stderr[-4000:],
            }
        )
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", default=".", help="Project root")
    parser.add_argument("--run", action="store_true", help="Execute checks")
    parser.add_argument("--json", action="store_true", help="Print JSON")
    args = parser.parse_args()

    project = Path(args.project).resolve()
    manager = detect_package_manager(project)
    checks = build_checks(project)
    payload: dict[str, object] = {
        "stack": "node",
        "project": str(project),
        "package_manager": manager,
        "checks": checks,
        "executed": bool(args.run),
    }
    if args.run:
        payload["results"] = run_checks(project, checks)

    if args.json:
        print(json.dumps(payload, ensure_ascii=True))
        return

    print("stack=node")
    print(f"project={project}")
    print("checks=" + "; ".join(checks))
    if args.run:
        failures = [r for r in payload["results"] if isinstance(r, dict) and r.get("code") != 0]  # type: ignore[index]
        print(f"failures={len(failures)}")
        raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
