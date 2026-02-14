# Operacoes

Comando principal de distribuicao:

```bash
npx @codex-workflow/cw
```

Comandos recomendados:

- `npx @codex-workflow/cw doctor`
- `npx @codex-workflow/cw --dry-run`
- `python scripts/codexwf.py status`
- `python scripts/codexwf.py validate --tests`
- `python scripts/codexwf.py docs-sync --build`

Fallback Windows:

```bash
npx @codex-workflow/cw --python-exec python
```

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
7. run `node tests/test_cw_cli_node.js`
