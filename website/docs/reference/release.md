# Release

## Fluxo local automatizado

Dry run:

```bash
python scripts/release_automation.py --version 1.1.0
```

Aplicar changelog + commit + tag + push:

```bash
python scripts/release_automation.py --version 1.1.0 --apply --commit --tag --push
```

## GitHub Actions

Arquivo:

- `.github/workflows/release.yml`

Suporta:

- `workflow_dispatch`
- publicacao automatica por `push` de tag `v*`

Se existir `docs/releases/<tag>.md`, esse arquivo vira corpo do release.
Caso contrario, usa `CHANGELOG.md`.
