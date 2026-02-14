# Release

```bash
python scripts/release_automation.py --version 1.1.0 --apply --commit --tag --push
```

Workflow: `.github/workflows/release.yml`.

- publica npm en push de tag `v*` cuando `NPM_TOKEN` esta configurado.
- sincroniza version de `package.json` durante el corte de release.
- valida que la tag `vX.Y.Z` coincida con `package.json` antes de publicar.
