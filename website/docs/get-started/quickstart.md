# Quickstart

## 1) Trigger workflows explicitly

Examples:

- `Use codex-workflows in /orchestrate and execute this goal: harden auth flow with tests`
- `Use codex-workflows in /debug and investigate an intermittent login failure`
- `Use codex-workflows in /plan for this feature roadmap`

## 2) Optional: bootstrap local `.agent`

Default profile (`codex-native`):

```bash
python ~/.codex/skills/codex-workflows/scripts/bootstrap_project_agent.py --project .
```

Compatibility profile:

```bash
python ~/.codex/skills/codex-workflows/scripts/bootstrap_project_agent.py --project . --profile antigravity-compat
```

Minimal profile:

```bash
python ~/.codex/skills/codex-workflows/scripts/bootstrap_project_agent.py --project . --profile minimal
```

## 3) Route request intent

```bash
python ~/.codex/skills/codex-workflows/scripts/route_workflow.py \
  "add secure login with tests and release notes" \
  --json
```

## 4) Validate by stack

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

## 5) Validate codex-native workflow quality

```bash
python ~/.codex/skills/codex-workflows/scripts/check_codex_native_quality.py \
  --native ~/.codex/skills/codex-workflows/templates/codex-native/.agent/workflows \
  --compat ~/.codex/skills/codex-workflows/packs/antigravity-compat/.agent/workflows
```
