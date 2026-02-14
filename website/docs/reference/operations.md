# Operations

Primary distribution command:

```bash
npx @codex-workflow/cw
```

Recommended operational commands:

- `npx @codex-workflow/cw doctor`
- `npx @codex-workflow/cw --dry-run`
- `python scripts/codexwf.py status`
- `python scripts/codexwf.py validate --tests`
- `python scripts/codexwf.py docs-sync --build`

Windows fallback:

```bash
npx @codex-workflow/cw --python-exec python
```

Legacy skill-ops command:

```bash
python skills/codex-workflows/scripts/codex_workflows_ops.py <command>
```

Main commands:

- `build-manifest`
- `check-drift`
- `check-workflows`
- `check-codex-native`
- `check-codex-assets`
- `benchmark`
- `bootstrap`
- `sync-pack`
- `release`

## Recommended maintenance routine

1. `sync_compat_pack.py`
2. `build_compat_manifest.py`
3. `check_compat_drift.py`
4. `check_workflow_parity.py`
5. `check_codex_native_quality.py`
6. `check_codex_native_assets.py`
7. `python -m unittest discover -s tests -p "test_*.py"`
8. `python scripts/ci_validate_skill.py --skills-root skills`
9. `node tests/test_cw_cli_node.js`

Detailed source:

- `docs/OPERATIONS.md`
