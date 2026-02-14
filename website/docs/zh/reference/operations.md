# 运维

主分发命令：

```bash
npx @codex-workflow/cw
```

推荐命令：

- `npx @codex-workflow/cw doctor`
- `npx @codex-workflow/cw --dry-run`
- `python scripts/codexwf.py status`
- `python scripts/codexwf.py validate --tests`
- `python scripts/codexwf.py docs-sync --build`

Windows 回退：

```bash
npx @codex-workflow/cw --python-exec python
```

技能遗留命令：

```bash
python skills/codex-workflows/scripts/codex_workflows_ops.py <command>
```

推荐例行流程：

1. sync pack
2. rebuild manifest
3. run drift/parity checks
4. run codex-native quality check
5. run codex-native assets check
6. run tests and skill validation
7. run `node tests/test_cw_cli_node.js`

完整说明见：`docs/OPERATIONS.md`。
