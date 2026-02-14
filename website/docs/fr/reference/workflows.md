# Workflows

Catalogue:

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

Pattern recommande:

- `cw /<workflow> <objectif>`
- `codex-workflow /<workflow> <objectif>`
- `codex-workflows /<workflow> <objectif>`
- `Use codex-workflows in /<workflow> and <objective>`

Commandes utilitaires:

- `cw /help` -> affiche l'aide d'activation
- `cw /examples` -> liste workflows et exemples

Profil par defaut: `codex-native`.

Compatibilite uniquement opt-in via `--profile antigravity-compat`.

Workflows natifs reecrits:

- `skills/codex-workflows/templates/codex-native/.agent/workflows/*.md`
- `skills/codex-workflows/templates/codex-native/.agent/agents/*.md`
- `skills/codex-workflows/templates/codex-native/.agent/skills/*/SKILL.md`

Checks qualite:

- parity compat:
  - `python skills/codex-workflows/scripts/check_workflow_parity.py --references skills/codex-workflows/references/workflows --native skills/codex-workflows/templates/codex-native/.agent/workflows --template skills/codex-workflows/templates/.agent/workflows --pack skills/codex-workflows/packs/antigravity-compat/.agent/workflows`
- qualite codex-native:
  - `python skills/codex-workflows/scripts/check_codex_native_quality.py --native skills/codex-workflows/templates/codex-native/.agent/workflows --compat skills/codex-workflows/packs/antigravity-compat/.agent/workflows --max-similarity 0.35`
- actifs codex-native:
  - `python skills/codex-workflows/scripts/check_codex_native_assets.py --native-root skills/codex-workflows/templates/codex-native/.agent --min-agents 20 --min-skills 37`


