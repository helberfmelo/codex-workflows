# Source: docs/RULES.md

# Rules Model

This repository uses a layered rules model for the `codex-native` profile.

Rules are designed to make execution more deterministic and auditable while keeping domain flexibility.

## Scope

Rules live at:

- `skills/codex-workflows/templates/codex-native/.agent/rules/`

The model has three layers:

1. Global rules
- directory: `rules/global/`
- applies to every workflow and domain

2. Domain rules
- directory: `rules/domains/`
- activated when relevant domains are in scope (for example backend, security, QA, game development)

3. Workflow rules
- directory: `rules/workflows/`
- one rule file per workflow contract in `workflows/*.md`

## Rule Resolution

Resolution order is cumulative:

1. Load `rules/CODEX.md`
2. Merge `rules/global/*.md`
3. Merge matching `rules/domains/*.md`
4. Enforce selected `rules/workflows/<workflow>.md`

Workflow rules are final execution gates for phase behavior.

## Validation

The layered model is enforced by:

- `python skills/codex-workflows/scripts/check_codex_native_rules.py --native-root skills/codex-workflows/templates/codex-native/.agent`

Checks include:

- entry rule presence (`rules/CODEX.md`)
- minimum global and domain rule counts
- minimum content size to avoid placeholder stubs
- one-to-one workflow rule coverage for `workflows/*.md`

CI also runs this gate in `.github/workflows/ci.yml`.

## Maintenance

When adding or renaming workflows:

1. update `templates/codex-native/.agent/workflows/*.md`
2. add or rename matching file in `templates/codex-native/.agent/rules/workflows/*.md`
3. run:
`python skills/codex-workflows/scripts/check_codex_native_rules.py --native-root skills/codex-workflows/templates/codex-native/.agent`
