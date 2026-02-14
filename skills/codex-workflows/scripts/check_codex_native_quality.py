#!/usr/bin/env python3
"""Validate codex-native workflow quality and differentiation from compat baseline."""
from __future__ import annotations

import argparse
from difflib import SequenceMatcher
from pathlib import Path


EXPECTED_WORKFLOWS = {
    "brainstorm.md": [
        "## Objective",
        "## Discovery Inputs",
        "## Option Generation Rules",
        "## Output Contract",
        "## Quality Bar",
    ],
    "plan.md": [
        "## Objective",
        "## Planning Intake",
        "## Required Plan Sections",
        "## Output Contract",
        "## Definition of Done for /plan",
    ],
    "create.md": [
        "## Objective",
        "## Entry Criteria",
        "## Delivery Phases",
        "## Output Contract",
        "## Quality Bar",
    ],
    "enhance.md": [
        "## Objective",
        "## Baseline First",
        "## Enhancement Flow",
        "## Output Contract",
        "## Quality Bar",
    ],
    "game-dev.md": [
        "## Objective",
        "## Game Delivery Inputs",
        "## Development Loop",
        "## Output Contract",
        "## Quality Bar",
    ],
    "roblox-game-dev.md": [
        "## Objective",
        "## Roblox Scope Inputs",
        "## Roblox Build Protocol",
        "## Output Contract",
        "## Quality Bar",
    ],
    "debug.md": [
        "## Objective",
        "## Investigation Protocol",
        "## Output Contract",
        "## Root Cause Closure Criteria",
    ],
    "test.md": [
        "## Objective",
        "## Risk-Based Test Planning",
        "## Execution Protocol",
        "## Output Contract",
        "## Quality Bar",
    ],
    "deploy.md": [
        "## Objective",
        "## Pre-Deploy Checklist",
        "## Rollout Strategy",
        "## Output Contract",
        "## Quality Bar",
    ],
    "preview.md": [
        "## Objective",
        "## Preview Setup",
        "## Validation Flow",
        "## Output Contract",
        "## Quality Bar",
    ],
    "status.md": [
        "## Objective",
        "## Reporting Dimensions",
        "## Output Contract",
        "## Quality Bar",
    ],
    "orchestrate.md": [
        "## Objective",
        "## Trigger Criteria",
        "## Four-Phase Protocol",
        "## Output Contract",
        "## Orchestration Quality Bar",
    ],
    "ui-ux-pro-max.md": [
        "## Objective",
        "## Design Principles",
        "## Design Sprint Protocol",
        "## Output Contract",
        "## Quality Bar",
    ],
}


def normalize_text(content: str) -> str:
    return content.replace("\r\n", "\n").replace("\r", "\n").strip()


def validate(native_dir: Path, compat_dir: Path, min_lines: int, max_similarity: float) -> list[str]:
    errors: list[str] = []

    for filename, required_sections in EXPECTED_WORKFLOWS.items():
        native_file = native_dir / filename
        compat_file = compat_dir / filename

        if not native_file.exists():
            errors.append(f"missing native workflow: {filename}")
            continue
        if not compat_file.exists():
            errors.append(f"missing compat workflow for comparison: {filename}")
            continue

        native_text = native_file.read_text(encoding="utf-8")
        compat_text = compat_file.read_text(encoding="utf-8")
        native_norm = normalize_text(native_text)
        compat_norm = normalize_text(compat_text)

        if normalize_text(native_text.split("\n", 1)[0]) != "---":
            errors.append(f"frontmatter missing at top: {filename}")

        line_count = len(native_text.splitlines())
        if line_count < min_lines:
            errors.append(f"workflow too short ({line_count} < {min_lines}): {filename}")

        for section in required_sections:
            if section not in native_text:
                errors.append(f"missing section '{section}' in {filename}")

        if native_norm == compat_norm:
            errors.append(f"native workflow is identical to compat baseline: {filename}")
            continue

        similarity = SequenceMatcher(None, native_norm, compat_norm).ratio()
        if similarity > max_similarity:
            errors.append(
                f"native workflow too similar to compat baseline ({similarity:.4f} > {max_similarity:.4f}): {filename}"
            )

    extra_native = {p.name for p in native_dir.glob("*.md")} - set(EXPECTED_WORKFLOWS)
    if extra_native:
        errors.append(f"unexpected extra native workflows: {', '.join(sorted(extra_native))}")

    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--native",
        help="templates/codex-native/.agent/workflows directory",
    )
    parser.add_argument(
        "--compat",
        help="packs/antigravity-compat/.agent/workflows directory",
    )
    parser.add_argument("--min-lines", type=int, default=45)
    parser.add_argument("--max-similarity", type=float, default=0.35)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    native_dir = Path(args.native).resolve() if args.native else root / "templates" / "codex-native" / ".agent" / "workflows"
    compat_dir = Path(args.compat).resolve() if args.compat else root / "packs" / "antigravity-compat" / ".agent" / "workflows"

    errors = validate(
        native_dir=native_dir,
        compat_dir=compat_dir,
        min_lines=args.min_lines,
        max_similarity=args.max_similarity,
    )
    if errors:
        print("FAIL: codex-native quality check failed")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print(f"OK: codex-native quality passed ({len(EXPECTED_WORKFLOWS)} workflows)")


if __name__ == "__main__":
    main()
