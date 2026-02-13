# Quickstart

1. Activation explicite:
`Use codex-workflows in /orchestrate and <objective>`

2. Bootstrap local:

```bash
python ~/.codex/skills/codex-workflows/scripts/bootstrap_project_agent.py --project . --profile antigravity-compat
```

3. Validation stack:

```bash
python ~/.codex/skills/codex-node-validation-pack/scripts/validate_node_stack.py --project . --run
python ~/.codex/skills/codex-python-validation-pack/scripts/validate_python_stack.py --project . --run
python ~/.codex/skills/codex-rust-validation-pack/scripts/validate_rust_stack.py --project . --run
```
