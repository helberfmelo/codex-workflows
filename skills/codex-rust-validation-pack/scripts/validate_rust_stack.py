#!/usr/bin/env python3
"""Validate Rust projects with Cargo-aware checks."""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path


def _load_cargo_toml(project: Path) -> str:
    cargo = project / "Cargo.toml"
    if not cargo.exists():
        raise SystemExit(f"Cargo.toml not found under: {project}")
    return cargo.read_text(encoding="utf-8")


def build_checks(project: Path) -> list[str]:
    cargo_toml = _load_cargo_toml(project)
    is_workspace = "[workspace]" in cargo_toml

    checks = ["cargo fmt --all -- --check"]
    if is_workspace:
        checks.extend(
            [
                "cargo clippy --workspace --all-targets --all-features -- -D warnings",
                "cargo test --workspace --all-targets --all-features",
                "cargo build --workspace --release",
            ]
        )
    else:
        checks.extend(
            [
                "cargo clippy --all-targets --all-features -- -D warnings",
                "cargo test --all-targets --all-features",
                "cargo build --release",
            ]
        )

    if (project / "Cargo.lock").exists() and shutil.which("cargo-audit"):
        checks.append("cargo audit")
    return checks


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
    cargo_toml = _load_cargo_toml(project)
    checks = build_checks(project)
    payload: dict[str, object] = {
        "stack": "rust",
        "project": str(project),
        "workspace": "[workspace]" in cargo_toml,
        "checks": checks,
        "executed": bool(args.run),
    }
    if args.run:
        payload["results"] = run_checks(project, checks)

    if args.json:
        print(json.dumps(payload, ensure_ascii=True))
        return

    print("stack=rust")
    print(f"project={project}")
    print("checks=" + "; ".join(checks))
    if args.run:
        failures = [r for r in payload["results"] if isinstance(r, dict) and r.get("code") != 0]  # type: ignore[index]
        print(f"failures={len(failures)}")
        raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
