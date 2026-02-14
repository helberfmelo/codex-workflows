# 安装

## 前置要求

- 支持 skills 的 Codex
- 已安装 Python
- 可访问 GitHub

## 推荐：NPM all-in-one

```bash
npx @codex-workflow/cw
```

仅安装核心：

```bash
npx @codex-workflow/cw --core-only
```

环境诊断：

```bash
npx @codex-workflow/cw doctor
```

## 备选：Python 直接安装 All-in-One

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo helberfmelo/codex-workflows \
  --path \
    skills/codex-workflows \
    skills/codex-backend-pack \
    skills/codex-frontend-pack \
    skills/codex-security-pack \
    skills/codex-qa-pack \
    skills/codex-node-validation-pack \
    skills/codex-python-validation-pack \
    skills/codex-rust-validation-pack
```

统一 CLI 方式：

```bash
python scripts/codexwf.py install
```

## 可选 Composer 通道

```bash
composer codex:install-all
```

可选本地 bootstrap：

```bash
python scripts/codexwf.py init --project .
```

## 安装后

推荐激活方式：

- `cw /orchestrate <目标>`
- `cw /help`
- `cw /examples`
- `Use codex-workflows in /orchestrate and <objective>`
