# Workflows

Catalogo suportado:

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

Perfil padrao de bootstrap: `codex-native`.

Compatibilidade e opt-in via `--profile antigravity-compat`.

Os workflows nativos reescritos ficam em:

- `skills/codex-workflows/templates/codex-native/.agent/workflows/*.md`
- `skills/codex-workflows/templates/codex-native/.agent/agents/*.md`
- `skills/codex-workflows/templates/codex-native/.agent/skills/*/SKILL.md`

## Padrao recomendado de prompt

- `Use codex-workflows in /<workflow> and <objective>`
- `Use codex-workflows em /<workflow> e <objetivo>`

## Regras de roteamento

- ativacao explicita tem prioridade;
- tarefas multi-dominio tendem a `/orchestrate`;
- ambiguo tende a `/plan`.

## Checks de qualidade

- parity de compatibilidade:
  - `python skills/codex-workflows/scripts/check_workflow_parity.py --references skills/codex-workflows/references/workflows --native skills/codex-workflows/templates/codex-native/.agent/workflows --template skills/codex-workflows/templates/.agent/workflows --pack skills/codex-workflows/packs/antigravity-compat/.agent/workflows`
- qualidade codex-native:
  - `python skills/codex-workflows/scripts/check_codex_native_quality.py --native skills/codex-workflows/templates/codex-native/.agent/workflows --compat skills/codex-workflows/packs/antigravity-compat/.agent/workflows --max-similarity 0.35`
- ativos codex-native:
  - `python skills/codex-workflows/scripts/check_codex_native_assets.py --native-root skills/codex-workflows/templates/codex-native/.agent --min-agents 20 --min-skills 37`


