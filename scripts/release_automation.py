#!/usr/bin/env python3
"""Automate changelog cut, git tag, and optional push for releases."""
from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
from pathlib import Path


SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
RELEASE_HEADING_RE = re.compile(r"^## \[(?P<label>[^\]]+)\](?:\s+-\s+.+)?\s*$")


def is_semver(version: str) -> bool:
    return bool(SEMVER_RE.match(version))


def _find_unreleased_section(lines: list[str]) -> tuple[int, int]:
    start = -1
    for idx, line in enumerate(lines):
        if line.strip() == "## [Unreleased]":
            start = idx
            break
    if start < 0:
        raise ValueError("CHANGELOG.md is missing '## [Unreleased]' section")

    end = len(lines)
    for idx in range(start + 1, len(lines)):
        if RELEASE_HEADING_RE.match(lines[idx].strip()):
            end = idx
            break
    return start, end


def _release_exists(lines: list[str], version: str) -> bool:
    for line in lines:
        match = RELEASE_HEADING_RE.match(line.strip())
        if match and match.group("label") == version:
            return True
    return False


def _trim_blank_edges(lines: list[str]) -> list[str]:
    start = 0
    end = len(lines)
    while start < end and not lines[start].strip():
        start += 1
    while end > start and not lines[end - 1].strip():
        end -= 1
    return lines[start:end]


def _has_bullet(lines: list[str]) -> bool:
    return any(line.strip().startswith("- ") for line in lines)


def build_release_notes(version: str, release_date: str, body_lines: list[str]) -> str:
    notes = [f"# Release v{version}", "", f"Date: {release_date}", ""]
    notes.extend(body_lines)
    return "\n".join(notes).rstrip() + "\n"


def cut_release(changelog_text: str, version: str, release_date: str, allow_empty: bool = False) -> tuple[str, str]:
    if not is_semver(version):
        raise ValueError(f"invalid semantic version: {version}")

    lines = changelog_text.splitlines()
    if _release_exists(lines, version):
        raise ValueError(f"version already exists in changelog: {version}")

    unreleased_start, unreleased_end = _find_unreleased_section(lines)
    unreleased_body = _trim_blank_edges(lines[unreleased_start + 1 : unreleased_end])
    if not allow_empty and not _has_bullet(unreleased_body):
        raise ValueError("Unreleased section has no bullet entries to release")
    if not unreleased_body:
        unreleased_body = ["### Added", "", "- Nothing yet."]

    new_lines: list[str] = []
    new_lines.extend(lines[: unreleased_start + 1])
    new_lines.extend(["", "### Added", "", "- Nothing yet.", ""])
    new_lines.append(f"## [{version}] - {release_date}")
    new_lines.append("")
    new_lines.extend(unreleased_body)
    new_lines.append("")
    new_lines.extend(lines[unreleased_end:])

    new_text = "\n".join(new_lines).rstrip() + "\n"
    notes = build_release_notes(version, release_date, unreleased_body)
    return new_text, notes


def run_git(repo: Path, args: list[str]) -> None:
    subprocess.run(["git"] + args, cwd=repo, check=True)


def current_branch(repo: Path) -> str:
    out = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=repo, text=True)
    return out.strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True, help="Release version (semantic version, e.g. 1.2.0)")
    parser.add_argument("--date", default=dt.date.today().isoformat(), help="Release date (YYYY-MM-DD)")
    parser.add_argument("--repo", default=".", help="Repository root")
    parser.add_argument("--changelog", default="CHANGELOG.md", help="Changelog path (relative to repo)")
    parser.add_argument("--notes-out", help="Optional path for generated release notes")
    parser.add_argument("--allow-empty", action="store_true", help="Allow release when Unreleased has no bullets")
    parser.add_argument("--apply", action="store_true", help="Write changes to disk")
    parser.add_argument("--commit", action="store_true", help="Create commit after changelog update (requires --apply)")
    parser.add_argument("--tag", action="store_true", help="Create annotated tag (requires --apply)")
    parser.add_argument("--push", action="store_true", help="Push current branch and tag if created (requires --apply)")
    parser.add_argument("--tag-prefix", default="v", help="Tag prefix (default: v)")
    parser.add_argument("--remote", default="origin", help="Git remote name when --push is used")
    parser.add_argument("--commit-message", default="chore(release): v{version}", help="Commit message template")
    parser.add_argument("--tag-message", default="Release v{version}", help="Tag annotation message template")
    args = parser.parse_args()

    if (args.commit or args.tag or args.push) and not args.apply:
        raise SystemExit("--commit/--tag/--push require --apply")

    repo = Path(args.repo).resolve()
    changelog = (repo / args.changelog).resolve()
    if not changelog.exists():
        raise SystemExit(f"changelog file not found: {changelog}")

    old_text = changelog.read_text(encoding="utf-8")
    new_text, release_notes = cut_release(old_text, args.version, args.date, allow_empty=args.allow_empty)
    tag_name = f"{args.tag_prefix}{args.version}"

    if not args.apply:
        print("mode=dry-run")
        print(f"repo={repo}")
        print(f"changelog={changelog}")
        print(f"version={args.version}")
        print(f"tag={tag_name}")
        print("result=ready")
        return

    changelog.write_text(new_text, encoding="utf-8")
    print(f"updated={changelog}")

    notes_path: Path | None = None
    if args.notes_out:
        notes_path = Path(args.notes_out).resolve()
        notes_path.parent.mkdir(parents=True, exist_ok=True)
        notes_path.write_text(release_notes, encoding="utf-8")
        print(f"release_notes={notes_path}")

    if args.commit:
        run_git(repo, ["add", str(changelog)])
        if notes_path is not None and notes_path.is_relative_to(repo):
            run_git(repo, ["add", str(notes_path)])
        run_git(repo, ["commit", "-m", args.commit_message.format(version=args.version)])
        print("git_commit=ok")

    if args.tag:
        run_git(
            repo,
            [
                "tag",
                "-a",
                tag_name,
                "-m",
                args.tag_message.format(version=args.version),
            ],
        )
        print(f"git_tag={tag_name}")

    if args.push:
        branch = current_branch(repo)
        run_git(repo, ["push", args.remote, branch])
        if args.tag:
            run_git(repo, ["push", args.remote, tag_name])
        print(f"git_push={args.remote}/{branch}")


if __name__ == "__main__":
    main()
