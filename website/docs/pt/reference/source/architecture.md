# Source: docs/ARCHITECTURE.md

# Architecture

## Goal

Provide a workflow operating system for GPT Codex in VS Code with:

- intent routing
- phase-based execution
- orchestration gates
- reusable local project templates

## Layers

1. Skill Core
- `skills/codex-workflows/SKILL.md`
- Activation and top-level execution contract

2. Routing and Governance
- `references/routing/intent-matrix.md`
- `references/orchestration/phase-gates.md`
- explicit activations via `cw /<workflow>` and `codex-workflow(s) /<workflow>`
- utility commands via `cw /help` and `cw /examples`

3. Workflow Knowledge Base
- `references/workflows/*.md`
- `references/templates/output-templates.md`
- References are codex-native contracts (mirrored from `templates/codex-native/.agent/workflows`).
- Catalog includes general software workflows plus game-specific `/game-dev` and `/roblox-game-dev`.

4. Automation Scripts
- `scripts/route_workflow.py`
- `scripts/route_workflow_fast.py`
- `scripts/routing_data.py`
- `scripts/bootstrap_project_agent.py`
- `scripts/sync_compat_pack.py`
- `scripts/build_compat_manifest.py`
- `scripts/check_compat_drift.py`
- `scripts/check_workflow_parity.py`
- `scripts/check_codex_native_quality.py`
- `scripts/check_codex_native_assets.py`
- `scripts/benchmark_router.py`
- `scripts/codex_workflows_ops.py`

5. Project Template
- `templates/codex-native/.agent/...` (default independent codex-native profile)
- native `agents/*.md` capability catalog
- native `skills/*/SKILL.md` capability catalog
- `templates/.agent/...` (full template baseline)
- `templates/minimal/.agent/...` (lightweight starter)
- Bootstraps local workflow files for projects without `.agent`

6. Compatibility Pack
- `packs/antigravity-compat/.agent/...`
- Full compatibility profile for projects that want Antigravity-like depth in Codex

7. Governance and Quality
- `compat/manifest.json` for drift control
- `.github/workflows/ci.yml` for automated checks
- Split parity gate via `check_workflow_parity.py`:
  - references <-> codex-native template
  - compat template <-> compat pack
- Codex-native workflow quality gate via `check_codex_native_quality.py`
- Codex-native structural gate via `check_codex_native_assets.py`
- Stack CI matrix (Node/Python/Rust) running real fixture checks
- `tests/` for script correctness

8. Domain Packs
- `skills/codex-backend-pack`
- `skills/codex-frontend-pack`
- `skills/codex-security-pack`
- `skills/codex-qa-pack`

9. Stack Validation Packs
- `skills/codex-node-validation-pack`
- `skills/codex-python-validation-pack`
- `skills/codex-rust-validation-pack`
- Stack-aware validation scripts for deterministic quality checks

10. Release Automation
- `scripts/release_automation.py`
- `.github/workflows/release.yml`
- Automated changelog cut + tag + release publishing flow

11. End-to-End Example Catalog
- `examples/node-auth-api/README.md`
- `examples/python-fastapi-orders/README.md`
- `examples/rust-events-cli/README.md`
- `examples/projects/` runnable fixtures used by CI stack matrix

12. All-in-One Installation
- `scripts/install_all_in_one.py`
- `scripts/codexwf.py` (`install` command)
- One-command installer orchestration for core + domain + stack packs

13. Web Documentation Portal
- `website/` (VitePress portal)
- EN + PT-BR + ES + FR + ZH locales
- `.github/workflows/docs.yml` for GitHub Pages deployment
- `website/scripts/sync_reference_docs.py` for mirrored technical references

14. Composer Wrapper Channel
- `composer.json`
- `scripts/composer_install.php`
- Optional PHP-native command surface for invoking official Codex installer

15. Community Governance
- `.github/ISSUE_TEMPLATE/*`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/CODEOWNERS`
- `docs/COMMUNITY.md`

## Execution Model

User request -> route workflow -> run phases -> validate -> report

For complex tasks:

User request -> /orchestrate -> discovery -> planning gate -> implementation -> verification -> synthesis
