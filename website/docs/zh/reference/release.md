# 发布

```bash
python scripts/release_automation.py --version 1.1.0 --apply --commit --tag --push
```

Workflow: `.github/workflows/release.yml`。

- 配置 `NPM_TOKEN` 后，`v*` 标签推送会自动发布 npm。
- release cut 会同步 `package.json` 版本号。
- 发布前校验标签版本 `vX.Y.Z` 与 `package.json` 一致。
