# Source: docs/WORKFLOW_CONTRACT.md

# Workflow Contract

The repository has two explicit workflow tracks:

1. `codex-native` track (default runtime and references)
2. `compatibility` track (opt-in pack)

## Codex-native contract

The following locations must stay byte-aligned:

1. `skills/codex-workflows/references/workflows/*.md`
2. `skills/codex-workflows/templates/codex-native/.agent/workflows/*.md`

Rules:

- same filename set in both locations;
- same content checksum in both locations;
- all 13 workflow contracts present.

## Compatibility contract

The following locations must stay byte-aligned:

1. `skills/codex-workflows/templates/.agent/workflows/*.md`
2. `skills/codex-workflows/packs/antigravity-compat/.agent/workflows/*.md`

Rules:

- same filename set in both locations;
- same content checksum in both locations;
- compatibility mode only via `--profile antigravity-compat`.

## Differentiation contract

Codex-native workflows must remain clearly distinct from compatibility workflows.

Rules:

- non-identical content per workflow;
- required codex-native structure sections present;
- max similarity ratio versus compatibility baseline must stay below threshold.

## Validation commands

Split parity check:

`python skills/codex-workflows/scripts/check_workflow_parity.py --references skills/codex-workflows/references/workflows --native skills/codex-workflows/templates/codex-native/.agent/workflows --template skills/codex-workflows/templates/.agent/workflows --pack skills/codex-workflows/packs/antigravity-compat/.agent/workflows`

Codex-native quality and anti-copy gate:

`python skills/codex-workflows/scripts/check_codex_native_quality.py --native skills/codex-workflows/templates/codex-native/.agent/workflows --compat skills/codex-workflows/packs/antigravity-compat/.agent/workflows --max-similarity 0.35`

## Why this exists

This contract keeps compatibility stable for opt-in users while protecting the default codex-native experience from copy-like drift.

