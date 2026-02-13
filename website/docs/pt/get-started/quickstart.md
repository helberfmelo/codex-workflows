# Quickstart

## 1) Acione workflow explicitamente

- `Use codex-workflows em /orchestrate e execute este objetivo: hardening de autenticacao com testes`
- `Use codex-workflows em /debug e investigue falha de login`
- `Use codex-workflows em /plan para este roadmap`

## 2) Bootstrap local `.agent` (opcional)

Perfil padrao (`codex-native`):

```bash
python ~/.codex/skills/codex-workflows/scripts/bootstrap_project_agent.py --project .
```

Este caminho padrao e independente do pack de compatibilidade.

Perfil de compatibilidade:

```bash
python ~/.codex/skills/codex-workflows/scripts/bootstrap_project_agent.py --project . --profile antigravity-compat
```

Perfil minimo:

```bash
python ~/.codex/skills/codex-workflows/scripts/bootstrap_project_agent.py --project . --profile minimal
```

## 3) Classificar intent

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

## 5) Validar qualidade do trilho codex-native

```bash
python ~/.codex/skills/codex-workflows/scripts/check_codex_native_quality.py \
  --native ~/.codex/skills/codex-workflows/templates/codex-native/.agent/workflows \
  --compat ~/.codex/skills/codex-workflows/packs/antigravity-compat/.agent/workflows \
  --max-similarity 0.35
```


