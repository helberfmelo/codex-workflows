#!/usr/bin/env python3
"""Validate Python projects with metadata-aware checks."""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

try:
    import tomllib  # type: ignore[attr-defined]
except ModuleNotFoundError:  # pragma: no cover - for very old Python runtimes
    tomllib = None


PROJECT_MARKERS = (
    "pyproject.toml",
    "setup.py",
    "requirements.txt",
    "requirements-dev.txt",
    "Pipfile",
)


def _contains_python_source(project: Path) -> bool:
    for candidate in (project, project / "src", project / "app", project / "tests"):
        if candidate.exists() and any(candidate.rglob("*.py")):
            return True
    return False


def _is_python_project(project: Path) -> bool:
    if any((project / marker).exists() for marker in PROJECT_MARKERS):
        return True
    return _contains_python_source(project)


def _load_pyproject(project: Path) -> tuple[dict, str]:
    pyproject = project / "pyproject.toml"
    if not pyproject.exists():
        return {}, ""
    raw = pyproject.read_text(encoding="utf-8")
    if tomllib is None:
        return {}, raw.lower()
    try:
        parsed = tomllib.loads(raw)
    except Exception:
        parsed = {}
    return parsed, raw.lower()


def _tool_config(parsed: dict) -> dict:
    tool = parsed.get("tool", {})
    if isinstance(tool, dict):
        return tool
    return {}


def build_checks(project: Path) -> list[str]:
    if not _is_python_project(project):
        raise SystemExit(f"no Python project markers found under: {project}")

    parsed, raw_pyproject = _load_pyproject(project)
    tool = _tool_config(parsed)
    checks: list[str] = []

    if "ruff" in tool or "ruff" in raw_pyproject:
        checks.append("python -m ruff check .")
    if "black" in tool or "black" in raw_pyproject:
        checks.append("python -m black --check .")
    if "mypy" in tool or "mypy" in raw_pyproject:
        checks.append("python -m mypy .")

    has_tests = (project / "tests").exists() or "pytest" in raw_pyproject or "pytest" in tool
    if has_tests:
        checks.append("python -m pytest")

    if any((project / marker).exists() for marker in PROJECT_MARKERS):
        checks.append("python -m pip check")

    checks.append("python -m compileall -q .")
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
    checks = build_checks(project)
    payload: dict[str, object] = {
        "stack": "python",
        "project": str(project),
        "checks": checks,
        "executed": bool(args.run),
    }
    if args.run:
        payload["results"] = run_checks(project, checks)

    if args.json:
        print(json.dumps(payload, ensure_ascii=True))
        return

    print("stack=python")
    print(f"project={project}")
    print("checks=" + "; ".join(checks))
    if args.run:
        failures = [r for r in payload["results"] if isinstance(r, dict) and r.get("code") != 0]  # type: ignore[index]
        print(f"failures={len(failures)}")
        raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
