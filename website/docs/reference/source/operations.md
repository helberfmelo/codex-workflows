# Source: docs/OPERATIONS.md

# Operations Runbook

Use this runbook to maintain `codex-workflows`.

## Distribution quickstart

Install all packs in one command:

`python scripts/install_all_in_one.py`

Bootstrap local project instructions (default codex-native profile):

`python skills/codex-workflows/scripts/bootstrap_project_agent.py --project .`

Composer wrapper (optional for PHP teams):

`composer codex:install-all`

Preview without changes:

`python scripts/install_all_in_one.py --dry-run`

## Website quickstart

Run the docs portal locally:

`cd website && npm install && npm run docs:dev`

Build production static output:

`cd website && npm run docs:build`

Refresh mirrored technical docs:

`python website/scripts/sync_reference_docs.py`

## Quick commands

Unified CLI:

`python skills/codex-workflows/scripts/codex_workflows_ops.py <command>`

Available commands:

- `build-manifest`
- `check-drift`
- `check-workflows`
- `check-codex-native`
- `benchmark`
- `bootstrap`
- `sync-pack`
- `release`

## Typical maintenance cycle

1. Sync compatibility pack:
`python skills/codex-workflows/scripts/sync_compat_pack.py --source <path-to-.agent>`

2. Rebuild compatibility manifest:
`python skills/codex-workflows/scripts/build_compat_manifest.py --source <path-to-.agent> --pack skills/codex-workflows/packs/antigravity-compat/.agent --template-full skills/codex-workflows/templates/.agent --output skills/codex-workflows/compat/manifest.json`

3. Run consistency checks:
- `python skills/codex-workflows/scripts/check_compat_drift.py --manifest skills/codex-workflows/compat/manifest.json --pack skills/codex-workflows/packs/antigravity-compat/.agent --template-full skills/codex-workflows/templates/.agent`
- `python skills/codex-workflows/scripts/check_workflow_parity.py --references skills/codex-workflows/references/workflows --template skills/codex-workflows/templates/.agent/workflows --pack skills/codex-workflows/packs/antigravity-compat/.agent/workflows`
- `python skills/codex-workflows/scripts/check_codex_native_quality.py --native skills/codex-workflows/templates/codex-native/.agent/workflows --compat skills/codex-workflows/packs/antigravity-compat/.agent/workflows`

4. Run tests and validation:
- `python -m unittest discover -s tests -p "test_*.py"`
- `python scripts/ci_validate_skill.py --skills-root skills`
- `python scripts/install_all_in_one.py --dry-run`
- `cd website && npm run docs:build`

5. Run stack packs when applicable:
- Node: `python skills/codex-node-validation-pack/scripts/validate_node_stack.py --project .`
- Python: `python skills/codex-python-validation-pack/scripts/validate_python_stack.py --project .`
- Rust: `python skills/codex-rust-validation-pack/scripts/validate_rust_stack.py --project .`

6. Release with automation:
- Dry run: `python scripts/release_automation.py --version 1.1.0`
- Apply + commit + tag + push: `python scripts/release_automation.py --version 1.1.0 --apply --commit --tag --push`
