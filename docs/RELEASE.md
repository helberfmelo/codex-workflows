# Release Runbook

## Pre-release checks

1. Skill validation:
`python scripts/ci_validate_skill.py --skills-root skills`

2. Unit tests:
`python -m unittest discover -s tests -p "test_*.py"`

3. Workflow split parity (native + compatibility tracks):
`python skills/codex-workflows/scripts/check_workflow_parity.py --references skills/codex-workflows/references/workflows --native skills/codex-workflows/templates/codex-native/.agent/workflows --template skills/codex-workflows/templates/.agent/workflows --pack skills/codex-workflows/packs/antigravity-compat/.agent/workflows`

4. Compatibility drift:
`python skills/codex-workflows/scripts/check_compat_drift.py --manifest skills/codex-workflows/compat/manifest.json --pack skills/codex-workflows/packs/antigravity-compat/.agent --template-full skills/codex-workflows/templates/.agent`

5. Codex-native workflow quality and anti-copy threshold:
`python skills/codex-workflows/scripts/check_codex_native_quality.py --native skills/codex-workflows/templates/codex-native/.agent/workflows --compat skills/codex-workflows/packs/antigravity-compat/.agent/workflows --max-similarity 0.35`

6. Codex-native structural assets:
`python skills/codex-workflows/scripts/check_codex_native_assets.py --native-root skills/codex-workflows/templates/codex-native/.agent --min-agents 20 --min-skills 37`

7. Router benchmark:
`python skills/codex-workflows/scripts/benchmark_router.py --iterations 10000`

Unified shortcut:

`python scripts/codexwf.py validate --tests --docs`

## Automated release (recommended)

Dry-run changelog cut:

`python scripts/release_automation.py --version 1.1.0`

Apply changelog update + commit + tag:

`python scripts/release_automation.py --version 1.1.0 --apply --commit --tag`

Push branch + tag:

`python scripts/release_automation.py --version 1.1.0 --apply --commit --tag --push`

Optional release notes output:

`python scripts/release_automation.py --version 1.1.0 --apply --notes-out docs/releases/v1.1.0.md`

Behavior:

- Moves `## [Unreleased]` entries into `## [<version>] - <date>`.
- Resets `Unreleased` to a clean placeholder.
- Optionally commits, tags, and pushes.

## GitHub Actions release

Workflow: `.github/workflows/release.yml`

Trigger via `workflow_dispatch` with:

- `version`: semantic version (example `1.1.0`)
- `push_changes`: `true` to push and publish GitHub Release

The workflow:

1. validates skills and tests;
2. runs `scripts/release_automation.py` with commit/tag;
3. pushes commit/tag (if enabled);
4. publishes the GitHub Release with generated notes.

Tag-driven publish is also enabled:

- Pushing `v*` tags triggers automatic release publication.
- It uses `docs/releases/<tag>.md` when available.
- Fallback body is `CHANGELOG.md` if release notes file is missing.

## Docs portal publish

Workflow: `.github/workflows/docs.yml`

- Triggered by changes under `website/**`, `docs/**`, or `README.md`.
- Builds `website` with VitePress.
- Pushes static output to `gh-pages` branch.
- First-time setup: in GitHub Settings > Pages, select `gh-pages` as source branch.


