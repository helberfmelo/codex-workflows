# Workflows

Supported catalog:

- `/brainstorm`
- `/plan`
- `/create`
- `/enhance`
- `/game-dev`
- `/roblox-game-dev`
- `/debug`
- `/test`
- `/deploy`
- `/preview`
- `/status`
- `/orchestrate`
- `/ui-ux-pro-max`

Default bootstrap profile: `codex-native`.

Compatibility is opt-in via `--profile antigravity-compat`.

`codex-native` includes rewritten workflow contracts in:

- `skills/codex-workflows/templates/codex-native/.agent/workflows/*.md`
- `skills/codex-workflows/templates/codex-native/.agent/agents/*.md`
- `skills/codex-workflows/templates/codex-native/.agent/skills/*/SKILL.md`

## Recommended prompt pattern

For deterministic behavior, always use explicit skill + workflow:

- `Use codex-workflows in /<workflow> and <goal>`
- `Use codex-workflows in /<workflow> and <objective>`

## Routing rules

- explicit activation has priority;
- multi-domain requests tend to `/orchestrate`;
- ambiguous requests default to `/plan`.

## Quality checks

- compatibility parity:
  - `python skills/codex-workflows/scripts/check_workflow_parity.py --references skills/codex-workflows/references/workflows --native skills/codex-workflows/templates/codex-native/.agent/workflows --template skills/codex-workflows/templates/.agent/workflows --pack skills/codex-workflows/packs/antigravity-compat/.agent/workflows`
- codex-native quality:
  - `python skills/codex-workflows/scripts/check_codex_native_quality.py --native skills/codex-workflows/templates/codex-native/.agent/workflows --compat skills/codex-workflows/packs/antigravity-compat/.agent/workflows --max-similarity 0.35`
- codex-native assets:
  - `python skills/codex-workflows/scripts/check_codex_native_assets.py --native-root skills/codex-workflows/templates/codex-native/.agent --min-agents 20 --min-skills 37`

Reference files:

- `skills/codex-workflows/scripts/route_workflow.py`
- `skills/codex-workflows/scripts/route_workflow_fast.py`
- `skills/codex-workflows/references/workflow-playbook.md`


