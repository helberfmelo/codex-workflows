#!/usr/bin/env python3
"""Validate codex-native layered rules quality and coverage."""
from __future__ import annotations

import argparse
from pathlib import Path


def list_md_files(path: Path) -> list[Path]:
    if not path.exists():
        return []
    return sorted([p for p in path.glob("*.md") if p.is_file()])


def stem_set(paths: list[Path]) -> set[str]:
    return {p.stem for p in paths}


def validate_rules(
    native_root: Path,
    *,
    min_global: int = 4,
    min_domain: int = 6,
    min_rule_bytes: int = 120,
) -> list[str]:
    errors: list[str] = []

    rules_root = native_root / "rules"
    workflows_root = native_root / "workflows"
    codex_entry = rules_root / "CODEX.md"
    global_root = rules_root / "global"
    domain_root = rules_root / "domains"
    workflow_rules_root = rules_root / "workflows"

    if not codex_entry.exists():
        errors.append("missing entry rule: rules/CODEX.md")
    elif codex_entry.stat().st_size < min_rule_bytes:
        errors.append("rules/CODEX.md is too small for a robust entry rule")

    global_rules = list_md_files(global_root)
    if len(global_rules) < min_global:
        errors.append(f"expected at least {min_global} global rules, found {len(global_rules)}")
    for rule in global_rules:
        if rule.stat().st_size < min_rule_bytes:
            errors.append(f"global rule too small: {rule.name}")

    domain_rules = list_md_files(domain_root)
    if len(domain_rules) < min_domain:
        errors.append(f"expected at least {min_domain} domain rules, found {len(domain_rules)}")
    for rule in domain_rules:
        if rule.stat().st_size < min_rule_bytes:
            errors.append(f"domain rule too small: {rule.name}")

    workflow_rules = list_md_files(workflow_rules_root)
    workflow_specs = list_md_files(workflows_root)
    if not workflow_specs:
        errors.append("no workflow specs found in native_root/workflows")
    if not workflow_rules:
        errors.append("no workflow rules found in native_root/rules/workflows")

    missing_rules = sorted(stem_set(workflow_specs) - stem_set(workflow_rules))
    if missing_rules:
        errors.append(f"missing workflow rules for: {', '.join(missing_rules)}")

    for rule in workflow_rules:
        if rule.stat().st_size < min_rule_bytes:
            errors.append(f"workflow rule too small: {rule.name}")

    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--native-root", required=True, help="Path to codex-native .agent root")
    parser.add_argument("--min-global", type=int, default=4)
    parser.add_argument("--min-domain", type=int, default=6)
    parser.add_argument("--min-rule-bytes", type=int, default=120)
    args = parser.parse_args()

    native_root = Path(args.native_root).resolve()
    errors = validate_rules(
        native_root,
        min_global=args.min_global,
        min_domain=args.min_domain,
        min_rule_bytes=args.min_rule_bytes,
    )
    if errors:
        print("FAIL: codex-native rules quality check failed")
        for err in errors:
            print(f"- {err}")
        raise SystemExit(1)
    print("OK: codex-native rules check passed")


if __name__ == "__main__":
    main()
