# 运维

统一命令：

```bash
python skills/codex-workflows/scripts/codex_workflows_ops.py <command>
```

主要命令：

- `build-manifest`
- `check-drift`
- `check-workflows`
- `check-codex-native`
- `benchmark`
- `bootstrap`
- `sync-pack`
- `release`

推荐例行流程：

1. sync pack
2. rebuild manifest
3. run drift/parity checks
4. run codex-native quality check
5. run tests and skill validation

完整说明见：`docs/OPERATIONS.md`。
