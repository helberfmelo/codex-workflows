# Operacoes

Comando unificado:

```bash
python skills/codex-workflows/scripts/codex_workflows_ops.py <command>
```

Comandos principais:

- `build-manifest`
- `check-drift`
- `check-workflows`
- `benchmark`
- `bootstrap`
- `sync-pack`
- `release`

Rotina recomendada:

1. sync pack
2. rebuild manifest
3. run drift/parity checks
4. run tests and skill validation
