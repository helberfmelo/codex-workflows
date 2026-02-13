# Operaciones

Comando unificado:

```bash
python skills/codex-workflows/scripts/codex_workflows_ops.py <command>
```

Comandos principales:

- `build-manifest`
- `check-drift`
- `check-workflows`
- `check-codex-native`
- `benchmark`
- `bootstrap`
- `sync-pack`
- `release`

Rutina recomendada:

1. sync pack
2. rebuild manifest
3. run drift/parity checks
4. run codex-native quality check
5. run tests and skill validation

Fuente completa: `docs/OPERATIONS.md`.
