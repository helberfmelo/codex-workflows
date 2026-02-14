# Codex-Native Project Agent Architecture

This profile is the default bootstrap path for Codex projects.

It is intentionally independent from compatibility packs and focuses on:

- codex-native workflow contracts;
- explicit validation evidence;
- lightweight local project scaffolding.

## Layout

- `workflows/`: detailed codex-native execution playbooks.
- `rules/`: high-level local operating rules.
- `scripts/`: local helper scripts used during preview and checks.
- `agents/`: codex-native specialist agents.
- `skills/`: codex-native domain skill catalog.

## Profiles

- `codex-native`: default profile for new projects.
- `minimal`: compact starter profile.
- `antigravity-compat`: optional interoperability profile.

## Structural Baseline

- `11` workflows
- `20` agents
- `37` skills

These minimums are enforced by `check_codex_native_assets.py` in CI and local validation commands.
