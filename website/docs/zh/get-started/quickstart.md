# 快速上手

1. 显式触发：
`Use codex-workflows in /orchestrate and <objective>`

2. 本地 bootstrap（默认 `codex-native`）：

```bash
python ~/.codex/skills/codex-workflows/scripts/bootstrap_project_agent.py --project .
```

该默认路径独立于兼容包。

兼容模式：

```bash
python ~/.codex/skills/codex-workflows/scripts/bootstrap_project_agent.py --project . --profile antigravity-compat
```

3. 按技术栈验证：

```bash
python ~/.codex/skills/codex-node-validation-pack/scripts/validate_node_stack.py --project . --run
python ~/.codex/skills/codex-python-validation-pack/scripts/validate_python_stack.py --project . --run
python ~/.codex/skills/codex-rust-validation-pack/scripts/validate_rust_stack.py --project . --run
```

4. 校验 codex-native 工作流质量：

```bash
python ~/.codex/skills/codex-workflows/scripts/check_codex_native_quality.py \
  --native ~/.codex/skills/codex-workflows/templates/codex-native/.agent/workflows \
  --compat ~/.codex/skills/codex-workflows/packs/antigravity-compat/.agent/workflows \
  --max-similarity 0.35
```

5. 校验 codex-native 结构化资产：

```bash
python ~/.codex/skills/codex-workflows/scripts/check_codex_native_assets.py \
  --native-root ~/.codex/skills/codex-workflows/templates/codex-native/.agent \
  --min-agents 20 \
  --min-skills 37
```



