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

Arquivo: `.github/workflows/release.yml`

- suporta `workflow_dispatch`;
- publica automaticamente por push de tag `v*`.
