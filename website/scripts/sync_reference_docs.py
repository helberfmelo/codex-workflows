#!/usr/bin/env python3
"""Sync selected root docs into website/docs/reference/source."""
from __future__ import annotations

from pathlib import Path


DOC_MAP = {
    "ARCHITECTURE.md": "architecture.md",
    "COMPARISON.md": "comparison.md",
    "WORKFLOW_CONTRACT.md": "workflow-contract.md",
    "OPERATIONS.md": "operations.md",
    "RELEASE.md": "release.md",
    "ROBUSTNESS-CHECKLIST.md": "robustness-checklist.md",
    "COMPATIBILITY.md": "compatibility.md",
    "PERFORMANCE.md": "performance.md",
}


def main() -> None:
    repo = Path(__file__).resolve().parents[2]
    docs_root = repo / "docs"
    target_roots = [
        repo / "website" / "docs" / "reference" / "source",
        repo / "website" / "docs" / "pt" / "reference" / "source",
    ]
    for root in target_roots:
        root.mkdir(parents=True, exist_ok=True)

    for source_name, target_name in DOC_MAP.items():
        source_file = docs_root / source_name
        if not source_file.exists():
            continue
        content = source_file.read_text(encoding="utf-8")
        header = f"# Source: docs/{source_name}\n\n"
        for target_root in target_roots:
            target_file = target_root / target_name
            target_file.write_text(header + content, encoding="utf-8")
            print(f"Synced: {source_file} -> {target_file}")


if __name__ == "__main__":
    main()
