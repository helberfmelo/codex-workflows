# Release Runbook

## Pre-release checks

1. Skill validation:
`python scripts/ci_validate_skill.py --skills-root skills`

2. Unit tests:
`python -m unittest discover -s tests -p "test_*.py"`

3. Workflow parity:
`python skills/codex-workflows/scripts/check_workflow_parity.py --references skills/codex-workflows/references/workflows --template skills/codex-workflows/templates/.agent/workflows --pack skills/codex-workflows/packs/antigravity-compat/.agent/workflows`

4. Compatibility drift:
`python skills/codex-workflows/scripts/check_compat_drift.py --manifest skills/codex-workflows/compat/manifest.json --pack skills/codex-workflows/packs/antigravity-compat/.agent --template-full skills/codex-workflows/templates/.agent`

5. Router benchmark:
`python skills/codex-workflows/scripts/benchmark_router.py --iterations 10000`

## Release steps

1. Update `CHANGELOG.md`.
2. Commit and push `main`.
3. Create Git tag (example `v1.1.0`).
4. Publish GitHub Release with highlights.
5. Verify installation instructions from README.
