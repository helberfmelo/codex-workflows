# Quickstart

1. Activar workflow explicito:
`cw /orchestrate harden auth flow with tests`
`cw /help`
`cw /examples`
`Use codex-workflows in /orchestrate and <objective>`
`Use codex-workflows in /game-dev and design a core gameplay loop`
`Use codex-workflows in /roblox-game-dev and secure RemoteEvent boundaries`

Quick wins por perfil:
`examples/quick-wins/README.md`

2. Bootstrap local (perfil por defecto `codex-native`):

```bash
python ~/.codex/skills/codex-workflows/scripts/bootstrap_project_agent.py --project .
```

Esta ruta por defecto es independiente del pack de compatibilidad.

Compatibilidad:

```bash
python ~/.codex/skills/codex-workflows/scripts/bootstrap_project_agent.py --project . --profile antigravity-compat
```

3. Validar por stack:

```bash
python ~/.codex/skills/codex-node-validation-pack/scripts/validate_node_stack.py --project . --run
python ~/.codex/skills/codex-python-validation-pack/scripts/validate_python_stack.py --project . --run
python ~/.codex/skills/codex-rust-validation-pack/scripts/validate_rust_stack.py --project . --run
```

4. Validar calidad de workflows codex-native:

```bash
python ~/.codex/skills/codex-workflows/scripts/check_codex_native_quality.py \
  --native ~/.codex/skills/codex-workflows/templates/codex-native/.agent/workflows \
  --compat ~/.codex/skills/codex-workflows/packs/antigravity-compat/.agent/workflows \
  --max-similarity 0.35
```

5. Validar activos estructurales de codex-native:

```bash
python ~/.codex/skills/codex-workflows/scripts/check_codex_native_assets.py \
  --native-root ~/.codex/skills/codex-workflows/templates/codex-native/.agent \
  --min-agents 20 \
  --min-skills 37
```



