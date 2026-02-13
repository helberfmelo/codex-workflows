#!/usr/bin/env python3
"""Sync selected root docs into website/docs/reference/source."""
from __future__ import annotations

from pathlib import Path


DOC_MAP = {
    "ARCHITECTURE.md": "architecture.md",
    "OPERATIONS.md": "operations.md",
    "RELEASE.md": "release.md",
    "ROBUSTNESS-CHECKLIST.md": "robustness-checklist.md",
    "COMPATIBILITY.md": "compatibility.md",
    "PERFORMANCE.md": "performance.md",
}


def main() -> None:
    repo = Path(__file__).resolve().parents[2]
    docs_root = repo / "docs"
    target_root = repo / "website" / "docs" / "reference" / "source"
    target_root.mkdir(parents=True, exist_ok=True)

    for source_name, target_name in DOC_MAP.items():
        source_file = docs_root / source_name
        if not source_file.exists():
            continue
        target_file = target_root / target_name
        content = source_file.read_text(encoding="utf-8")
        header = f"# Source: docs/{source_name}\n\n"
        target_file.write_text(header + content, encoding="utf-8")
        print(f"Synced: {source_file} -> {target_file}")


if __name__ == "__main__":
    main()
