# 运维

仓库统一 CLI：

```bash
python scripts/codexwf.py <command>
```

主要命令：

- `install`
- `init`
- `status`
- `validate`
- `docs-sync`

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

完整说明见：`docs/OPERATIONS.md`。
