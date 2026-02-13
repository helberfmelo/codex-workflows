#!/usr/bin/env python3
"""Repository-local skill validator for CI."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
NAME_RE = re.compile(r"^name:\s*(.+)\s*$", re.MULTILINE)
DESC_RE = re.compile(r"^description:\s*(.+)\s*$", re.MULTILINE)


def parse_frontmatter(skill_file: Path) -> tuple[str, str]:
    content = skill_file.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(content)
    if not m:
        raise ValueError(f"{skill_file}: missing YAML frontmatter")
    fm = m.group(1)
    n = NAME_RE.search(fm)
    d = DESC_RE.search(fm)
    if not n or not d:
        raise ValueError(f"{skill_file}: frontmatter must include name and description")
    return n.group(1).strip("\"' "), d.group(1).strip("\"' ")


def validate_skill_dir(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        errors.append(f"{skill_dir}: missing SKILL.md")
        return errors
    try:
        name, desc = parse_frontmatter(skill_file)
        if name != skill_dir.name:
            errors.append(f"{skill_file}: name '{name}' must match folder '{skill_dir.name}'")
        if not desc:
            errors.append(f"{skill_file}: description cannot be empty")
    except ValueError as exc:
        errors.append(str(exc))
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skills-root", default="skills", help="Root folder containing skill directories")
    args = parser.parse_args()

    root = Path(args.skills_root).resolve()
    if not root.exists():
        raise SystemExit(f"skills root does not exist: {root}")

    errors: list[str] = []
    skill_dirs = [p for p in root.iterdir() if p.is_dir()]
    if not skill_dirs:
        errors.append(f"no skills found under {root}")
    for skill_dir in sorted(skill_dirs):
        errors.extend(validate_skill_dir(skill_dir))

    if errors:
        print("FAIL: skill validation failed")
        for e in errors:
            print(f"- {e}")
        raise SystemExit(1)

    print(f"OK: validated {len(skill_dirs)} skill directories")


if __name__ == "__main__":
    main()

