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
- publica no npm por push de tag `v*` quando `NPM_TOKEN` esta configurado.

Guardrails:

- automacao sincroniza a versao do `package.json`;
- publicacao npm valida tag `vX.Y.Z` contra `package.json`.
