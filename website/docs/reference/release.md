# Release

## Local automated flow

Dry run:

```bash
python scripts/release_automation.py --version 1.1.0
```

Apply changelog + commit + tag + push:

```bash
python scripts/release_automation.py --version 1.1.0 --apply --commit --tag --push
```

## GitHub Actions

Arquivo:

- `.github/workflows/release.yml`

Supports:

- `workflow_dispatch`
- auto publish on `v*` tag push
- npm auto publish on `v*` tag push when `NPM_TOKEN` is configured

Guards:

- release automation syncs `package.json` version;
- npm publish checks tag version (`vX.Y.Z`) against `package.json`.

If `docs/releases/<tag>.md` exists, it is used as the release body.
Otherwise it falls back to `CHANGELOG.md`.
