# Operations

Unified repository CLI:

```bash
python scripts/codexwf.py <command>
```

Main commands:

- `install`
- `init`
- `status`
- `validate`
- `docs-sync`

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

Detailed source:

- `docs/OPERATIONS.md`
