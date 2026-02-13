# Workflow Contract

All workflow definitions must remain aligned across three runtime locations:

1. `skills/codex-workflows/references/workflows/*.md`
2. `skills/codex-workflows/templates/.agent/workflows/*.md`
3. `skills/codex-workflows/packs/antigravity-compat/.agent/workflows/*.md`

## Contract rules

- Same filename set in all three locations.
- Same content checksum in all three locations.
- No placeholder stub allowed in full profile files.

## Validation command

`python skills/codex-workflows/scripts/check_workflow_parity.py --references skills/codex-workflows/references/workflows --template skills/codex-workflows/templates/.agent/workflows --pack skills/codex-workflows/packs/antigravity-compat/.agent/workflows`

## Why this exists

Routing can load either references, template bootstrap, or compatibility pack content depending on context. Drift between these sources causes inconsistent behavior and lower quality responses.
