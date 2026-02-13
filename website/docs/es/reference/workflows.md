# Workflows

Catalogo:

- `/brainstorm`
- `/plan`
- `/create`
- `/enhance`
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

Workflows nativos reescritos:

- `skills/codex-workflows/templates/codex-native/.agent/workflows/*.md`

Checks de calidad:

- compat parity:
  - `python skills/codex-workflows/scripts/check_workflow_parity.py --references skills/codex-workflows/references/workflows --template skills/codex-workflows/templates/.agent/workflows --pack skills/codex-workflows/packs/antigravity-compat/.agent/workflows`
- calidad codex-native:
  - `python skills/codex-workflows/scripts/check_codex_native_quality.py --native skills/codex-workflows/templates/codex-native/.agent/workflows --compat skills/codex-workflows/packs/antigravity-compat/.agent/workflows`
