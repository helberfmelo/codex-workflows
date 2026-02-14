# Workflows

Catalogo:

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

Patron recomendado:

- `Use codex-workflows in /<workflow> and <objective>`

Perfil por defecto: `codex-native`.

Compatibilidad solo opt-in via `--profile antigravity-compat`.

Workflows nativos reescritos:

- `skills/codex-workflows/templates/codex-native/.agent/workflows/*.md`
- `skills/codex-workflows/templates/codex-native/.agent/agents/*.md`
- `skills/codex-workflows/templates/codex-native/.agent/skills/*/SKILL.md`

Checks de calidad:

- compat parity:
  - `python skills/codex-workflows/scripts/check_workflow_parity.py --references skills/codex-workflows/references/workflows --native skills/codex-workflows/templates/codex-native/.agent/workflows --template skills/codex-workflows/templates/.agent/workflows --pack skills/codex-workflows/packs/antigravity-compat/.agent/workflows`
- calidad codex-native:
  - `python skills/codex-workflows/scripts/check_codex_native_quality.py --native skills/codex-workflows/templates/codex-native/.agent/workflows --compat skills/codex-workflows/packs/antigravity-compat/.agent/workflows --max-similarity 0.35`
- activos codex-native:
  - `python skills/codex-workflows/scripts/check_codex_native_assets.py --native-root skills/codex-workflows/templates/codex-native/.agent --min-agents 20 --min-skills 37`


