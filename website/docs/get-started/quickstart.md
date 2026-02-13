# Quickstart

## 1) Ativar workflow explicitamente

Exemplos:

- `Use codex-workflows in /orchestrate and execute this goal: harden auth flow with tests`
- `Use codex-workflows em /debug e investigue falha intermitente de login`
- `Use codex-workflows in /plan for this feature roadmap`

## 2) Opcional: bootstrap local `.agent`

Perfil completo:

```bash
python ~/.codex/skills/codex-workflows/scripts/bootstrap_project_agent.py --project . --profile antigravity-compat
```

Perfil minimo:

```bash
python ~/.codex/skills/codex-workflows/scripts/bootstrap_project_agent.py --project . --profile minimal
```

## 3) Classificacao de intent

```bash
python ~/.codex/skills/codex-workflows/scripts/route_workflow.py \
  "add secure login with tests and release notes" \
  --json
```

## 4) Validar por stack

Node:

```bash
python ~/.codex/skills/codex-node-validation-pack/scripts/validate_node_stack.py --project . --run
```

Python:

```bash
python ~/.codex/skills/codex-python-validation-pack/scripts/validate_python_stack.py --project . --run
```

Rust:

```bash
python ~/.codex/skills/codex-rust-validation-pack/scripts/validate_rust_stack.py --project . --run
```
