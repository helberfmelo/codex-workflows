# Operations Runbook

Use this runbook to maintain `codex-workflows`.

## Quick commands

Unified CLI:

`python skills/codex-workflows/scripts/codex_workflows_ops.py <command>`

Available commands:

- `build-manifest`
- `check-drift`
- `check-workflows`
- `benchmark`
- `bootstrap`
- `sync-pack`

## Typical maintenance cycle

1. Sync compatibility pack:
`python skills/codex-workflows/scripts/sync_compat_pack.py --source <path-to-.agent>`

2. Rebuild compatibility manifest:
`python skills/codex-workflows/scripts/build_compat_manifest.py --source <path-to-.agent> --pack skills/codex-workflows/packs/antigravity-compat/.agent --template-full skills/codex-workflows/templates/.agent --output skills/codex-workflows/compat/manifest.json`

3. Run consistency checks:
- `python skills/codex-workflows/scripts/check_compat_drift.py --manifest skills/codex-workflows/compat/manifest.json --pack skills/codex-workflows/packs/antigravity-compat/.agent --template-full skills/codex-workflows/templates/.agent`
- `python skills/codex-workflows/scripts/check_workflow_parity.py --references skills/codex-workflows/references/workflows --template skills/codex-workflows/templates/.agent/workflows --pack skills/codex-workflows/packs/antigravity-compat/.agent/workflows`

4. Run tests and validation:
- `python -m unittest discover -s tests -p "test_*.py"`
- `python scripts/ci_validate_skill.py --skills-root skills`

5. Update docs/changelog and release.
