# Operacoes

CLI unificada do repositorio:

```bash
python scripts/codexwf.py <command>
```

Comandos principais:

- `install`
- `init`
- `status`
- `validate`
- `docs-sync`

Comando legado de operacoes do skill:

```bash
python skills/codex-workflows/scripts/codex_workflows_ops.py <command>
```

Rotina recomendada:

1. sync pack
2. rebuild manifest
3. run drift/parity checks
4. run codex-native quality check
5. run codex-native assets check
6. run tests and skill validation
