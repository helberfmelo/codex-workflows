# Quickstart

1. Activar workflow explicito:
`Use codex-workflows in /orchestrate and <objective>`

2. Bootstrap local (perfil por defecto `codex-native`):

```bash
python ~/.codex/skills/codex-workflows/scripts/bootstrap_project_agent.py --project .
```

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
  --compat ~/.codex/skills/codex-workflows/packs/antigravity-compat/.agent/workflows
```
