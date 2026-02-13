# 快速上手

1. 显式触发：
`Use codex-workflows in /orchestrate and <objective>`

2. 本地 bootstrap：

```bash
python ~/.codex/skills/codex-workflows/scripts/bootstrap_project_agent.py --project . --profile antigravity-compat
```

3. 按技术栈验证：

```bash
python ~/.codex/skills/codex-node-validation-pack/scripts/validate_node_stack.py --project . --run
python ~/.codex/skills/codex-python-validation-pack/scripts/validate_python_stack.py --project . --run
python ~/.codex/skills/codex-rust-validation-pack/scripts/validate_rust_stack.py --project . --run
```
