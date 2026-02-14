# 工作流

支持目录：

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

推荐提示词：

- `Use codex-workflows in /<workflow> and <objective>`

默认 profile：`codex-native`。

兼容模式仅在显式 `--profile antigravity-compat` 时启用。

原生重写工作流路径：

- `skills/codex-workflows/templates/codex-native/.agent/workflows/*.md`
- `skills/codex-workflows/templates/codex-native/.agent/agents/*.md`
- `skills/codex-workflows/templates/codex-native/.agent/skills/*/SKILL.md`

质量检查：

- compat parity:
  - `python skills/codex-workflows/scripts/check_workflow_parity.py --references skills/codex-workflows/references/workflows --native skills/codex-workflows/templates/codex-native/.agent/workflows --template skills/codex-workflows/templates/.agent/workflows --pack skills/codex-workflows/packs/antigravity-compat/.agent/workflows`
- codex-native quality:
  - `python skills/codex-workflows/scripts/check_codex_native_quality.py --native skills/codex-workflows/templates/codex-native/.agent/workflows --compat skills/codex-workflows/packs/antigravity-compat/.agent/workflows --max-similarity 0.35`
- codex-native assets:
  - `python skills/codex-workflows/scripts/check_codex_native_assets.py --native-root skills/codex-workflows/templates/codex-native/.agent --min-agents 20 --min-skills 37`


