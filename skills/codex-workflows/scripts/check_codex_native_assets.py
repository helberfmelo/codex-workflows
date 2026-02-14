#!/usr/bin/env python3
"""Validate codex-native template structural assets."""
from __future__ import annotations

import argparse
from pathlib import Path


EXPECTED_WORKFLOWS = {
    "brainstorm.md",
    "plan.md",
    "create.md",
    "enhance.md",
    "debug.md",
    "test.md",
    "deploy.md",
    "preview.md",
    "status.md",
    "orchestrate.md",
    "ui-ux-pro-max.md",
}


def validate(native_root: Path, min_agents: int, min_skills: int) -> list[str]:
    errors: list[str] = []

    required_paths = [
        native_root / "ARCHITECTURE.md",
        native_root / "rules" / "CODEX.md",
        native_root / "scripts" / "auto_preview.py",
        native_root / "workflows",
        native_root / "agents",
        native_root / "skills",
    ]
    for path in required_paths:
        if not path.exists():
            errors.append(f"missing required path: {path}")

    workflow_dir = native_root / "workflows"
    if workflow_dir.exists():
        names = {p.name for p in workflow_dir.glob("*.md")}
        missing = sorted(EXPECTED_WORKFLOWS - names)
        extra = sorted(names - EXPECTED_WORKFLOWS)
        if missing:
            errors.append(f"missing workflows: {', '.join(missing)}")
        if extra:
            errors.append(f"unexpected workflows: {', '.join(extra)}")

    agents_dir = native_root / "agents"
    if agents_dir.exists():
        agent_files = [p for p in agents_dir.glob("*.md") if p.is_file()]
        if len(agent_files) < min_agents:
            errors.append(f"insufficient native agents ({len(agent_files)} < {min_agents})")

    skills_dir = native_root / "skills"
    if skills_dir.exists():
        skill_dirs = [p for p in skills_dir.iterdir() if p.is_dir()]
        if len(skill_dirs) < min_skills:
            errors.append(f"insufficient native skills ({len(skill_dirs)} < {min_skills})")
        for skill_dir in sorted(skill_dirs):
            skill_file = skill_dir / "SKILL.md"
            if not skill_file.exists():
                errors.append(f"missing SKILL.md in native skill: {skill_dir.name}")
                continue
            content = skill_file.read_text(encoding="utf-8")
            if "name:" not in content or "description:" not in content:
                errors.append(f"invalid frontmatter in native skill: {skill_dir.name}")

    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--native-root",
        help="templates/codex-native/.agent root directory",
    )
    parser.add_argument("--min-agents", type=int, default=10)
    parser.add_argument("--min-skills", type=int, default=8)
    args = parser.parse_args()

    script_root = Path(__file__).resolve().parents[1]
    native_root = Path(args.native_root).resolve() if args.native_root else script_root / "templates" / "codex-native" / ".agent"

    errors = validate(native_root=native_root, min_agents=args.min_agents, min_skills=args.min_skills)
    if errors:
        print("FAIL: codex-native assets check failed")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("OK: codex-native assets check passed")


if __name__ == "__main__":
    main()
