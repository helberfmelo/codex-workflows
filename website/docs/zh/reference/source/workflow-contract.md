# Source: docs/WORKFLOW_CONTRACT.md

# Workflow Contract

The repository now has two workflow tracks:

1. `compatibility track` (strict parity)
2. `codex-native track` (default profile)

## Compatibility track contract

The following locations must stay byte-parity aligned:

1. `skills/codex-workflows/references/workflows/*.md`
2. `skills/codex-workflows/templates/.agent/workflows/*.md`
3. `skills/codex-workflows/packs/antigravity-compat/.agent/workflows/*.md`

Rules:

- same filename set in all three locations;
- same content checksum in all three locations;
- no placeholder stubs.

Validation:

`python skills/codex-workflows/scripts/check_workflow_parity.py --references skills/codex-workflows/references/workflows --template skills/codex-workflows/templates/.agent/workflows --pack skills/codex-workflows/packs/antigravity-compat/.agent/workflows`

## Codex-native track contract

The default bootstrap profile uses:

- `skills/codex-workflows/templates/codex-native/.agent/workflows/*.md`

Rules:

- all 11 workflow files must exist;
- each workflow must include required quality sections;
- each workflow must be non-identical to compatibility baseline counterpart;
- no workflow should be a short stub.

Validation:

`python skills/codex-workflows/scripts/check_codex_native_quality.py --native skills/codex-workflows/templates/codex-native/.agent/workflows --compat skills/codex-workflows/packs/antigravity-compat/.agent/workflows`

## Why this exists

This contract keeps compatibility behavior stable while allowing the default `codex-native` profile to evolve independently with stronger Codex-specific execution quality.
