#!/usr/bin/env python3
"""Unified operations CLI for codex-workflows maintenance."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run(args: list[str]) -> int:
    proc = subprocess.run([sys.executable] + args, check=False)
    return proc.returncode


def resolve_manifest_source(
    explicit_source: str | None,
    *,
    cwd: Path,
    repo_root: Path,
    pack_root: Path,
) -> tuple[Path, bool]:
    if explicit_source:
        source = Path(explicit_source).expanduser().resolve()
        if not source.exists():
            raise FileNotFoundError(f"Explicit --source path does not exist: {source}")
        return source, False

    local_source = (cwd / ".agent").resolve()
    if local_source.exists():
        return local_source, False

    repo_source = (repo_root / ".agent").resolve()
    if repo_source.exists():
        return repo_source, False

    return pack_root.resolve(), True


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("route")
    sub.add_parser("route-fast")

    p_bench = sub.add_parser("benchmark")
    p_bench.add_argument("--iterations", type=int, default=10000)

    p_bootstrap = sub.add_parser("bootstrap")
    p_bootstrap.add_argument("--project", default=".")
    p_bootstrap.add_argument(
        "--profile",
        default="codex-native",
        choices=("codex-native", "minimal", "antigravity-compat"),
    )
    p_bootstrap.add_argument("--force", action="store_true")

    p_sync = sub.add_parser("sync-pack")
    p_sync.add_argument("--source", required=True)

    p_release = sub.add_parser("release")
    p_release.add_argument("--version", required=True)
    p_release.add_argument("--apply", action="store_true")
    p_release.add_argument("--commit", action="store_true")
    p_release.add_argument("--tag", action="store_true")
    p_release.add_argument("--push", action="store_true")

    p_manifest = sub.add_parser("build-manifest")
    p_manifest.add_argument("--source", help="Optional source .agent directory override")
    sub.add_parser("check-drift")
    sub.add_parser("check-workflows")
    sub.add_parser("check-codex-native")
    sub.add_parser("check-codex-assets")

    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    scripts = root / "scripts"

    if args.cmd == "route":
        code = run([str(scripts / "route_workflow.py"), "example query", "--show-domains"])
        raise SystemExit(code)
    if args.cmd == "route-fast":
        code = run([str(scripts / "route_workflow_fast.py"), "example query", "--show-domains"])
        raise SystemExit(code)
    if args.cmd == "benchmark":
        code = run([str(scripts / "benchmark_router.py"), "--iterations", str(args.iterations)])
        raise SystemExit(code)
    if args.cmd == "bootstrap":
        cmd = [str(scripts / "bootstrap_project_agent.py"), "--project", args.project, "--profile", args.profile]
        if args.force:
            cmd.append("--force")
        code = run(cmd)
        raise SystemExit(code)
    if args.cmd == "sync-pack":
        code = run([str(scripts / "sync_compat_pack.py"), "--source", args.source])
        raise SystemExit(code)
    if args.cmd == "release":
        repo_root = Path(__file__).resolve().parents[3]
        cmd = [
            str(repo_root / "scripts" / "release_automation.py"),
            "--version",
            args.version,
        ]
        if args.apply:
            cmd.append("--apply")
        if args.commit:
            cmd.append("--commit")
        if args.tag:
            cmd.append("--tag")
        if args.push:
            cmd.append("--push")
        code = run(cmd)
        raise SystemExit(code)
    if args.cmd == "build-manifest":
        repo_root = Path(__file__).resolve().parents[3]
        pack_root = root / "packs" / "antigravity-compat" / ".agent"
        source_path, used_pack_fallback = resolve_manifest_source(
            args.source,
            cwd=Path.cwd(),
            repo_root=repo_root,
            pack_root=pack_root,
        )
        if used_pack_fallback:
            print(
                "WARNING: no local .agent source found; using compatibility pack as source for manifest build.",
                file=sys.stderr,
            )
        code = run(
            [
                str(scripts / "build_compat_manifest.py"),
                "--source",
                str(source_path),
                "--pack",
                str(pack_root),
                "--template-full",
                str(root / "templates" / ".agent"),
                "--output",
                str(root / "compat" / "manifest.json"),
            ]
        )
        raise SystemExit(code)
    if args.cmd == "check-drift":
        code = run(
            [
                str(scripts / "check_compat_drift.py"),
                "--manifest",
                str(root / "compat" / "manifest.json"),
                "--pack",
                str(root / "packs" / "antigravity-compat" / ".agent"),
                "--template-full",
                str(root / "templates" / ".agent"),
            ]
        )
        raise SystemExit(code)
    if args.cmd == "check-workflows":
        code = run(
            [
                str(scripts / "check_workflow_parity.py"),
                "--references",
                str(root / "references" / "workflows"),
                "--native",
                str(root / "templates" / "codex-native" / ".agent" / "workflows"),
                "--template",
                str(root / "templates" / ".agent" / "workflows"),
                "--pack",
                str(root / "packs" / "antigravity-compat" / ".agent" / "workflows"),
            ]
        )
        raise SystemExit(code)
    if args.cmd == "check-codex-native":
        code = run(
            [
                str(scripts / "check_codex_native_quality.py"),
                "--native",
                str(root / "templates" / "codex-native" / ".agent" / "workflows"),
                "--compat",
                str(root / "packs" / "antigravity-compat" / ".agent" / "workflows"),
                "--max-similarity",
                "0.35",
            ]
        )
        raise SystemExit(code)
    if args.cmd == "check-codex-assets":
        code = run(
            [
                str(scripts / "check_codex_native_assets.py"),
                "--native-root",
                str(root / "templates" / "codex-native" / ".agent"),
                "--min-agents",
                "20",
                "--min-skills",
                "37",
            ]
        )
        raise SystemExit(code)


if __name__ == "__main__":
    main()

