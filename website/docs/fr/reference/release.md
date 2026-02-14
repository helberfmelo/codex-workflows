# Release

```bash
python scripts/release_automation.py --version 1.1.0 --apply --commit --tag --push
```

Workflow: `.github/workflows/release.yml`.

- publication npm sur push de tag `v*` avec `NPM_TOKEN`.
- synchronisation de version `package.json` pendant le cut release.
- verification tag `vX.Y.Z` == version `package.json` avant publication.
