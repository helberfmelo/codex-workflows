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

## Rotina recomendada de manutencao

1. `sync_compat_pack.py`
2. `build_compat_manifest.py`
3. `check_compat_drift.py`
4. `check_workflow_parity.py`
5. `python -m unittest discover -s tests -p "test_*.py"`
6. `python scripts/ci_validate_skill.py --skills-root skills`

Fonte detalhada:

- `docs/OPERATIONS.md`
