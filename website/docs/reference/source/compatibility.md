# Source: docs/COMPATIBILITY.md

# Compatibility Operations

This project maintains a full Antigravity-compatible `.agent` tree in two places:

- `skills/codex-workflows/packs/antigravity-compat/.agent`
- `skills/codex-workflows/templates/.agent`

The first is the compatibility pack and the second is the compatibility baseline template.

Default project bootstrap now uses:

- `skills/codex-workflows/templates/codex-native/.agent` as independent source
- includes native `agents/` and `skills/` catalogs separate from compatibility content

Compatibility content is only used when `--profile antigravity-compat` is explicitly selected.

## Source of truth

Use a local Antigravity `.agent` snapshot as input source.

## Sync process

1. Sync pack from source:
`python skills/codex-workflows/scripts/sync_compat_pack.py --source <path-to-.agent>`

2. Copy updated pack to full template:
`Copy-Item -Recurse -Force skills/codex-workflows/packs/antigravity-compat/.agent/* skills/codex-workflows/templates/.agent`

3. Rebuild manifest:
`python skills/codex-workflows/scripts/build_compat_manifest.py --source <path-to-.agent> --pack skills/codex-workflows/packs/antigravity-compat/.agent --template-full skills/codex-workflows/templates/.agent --output skills/codex-workflows/compat/manifest.json`

4. Validate drift:
`python skills/codex-workflows/scripts/check_compat_drift.py --manifest skills/codex-workflows/compat/manifest.json --pack skills/codex-workflows/packs/antigravity-compat/.agent --template-full skills/codex-workflows/templates/.agent`

5. Validate workflow parity:
`python skills/codex-workflows/scripts/check_workflow_parity.py --references skills/codex-workflows/references/workflows --native skills/codex-workflows/templates/codex-native/.agent/workflows --template skills/codex-workflows/templates/.agent/workflows --pack skills/codex-workflows/packs/antigravity-compat/.agent/workflows`

## Notes

- `.pyc` and `__pycache__` files are intentionally excluded from manifests.
- Compatibility checks should pass locally before opening a release PR.
- `references/workflows` is part of the codex-native track, not the compatibility source of truth.

