# Comparison: Antigravity Kit vs Codex Workflows

Date: 2026-02-13

## Source baseline

Antigravity Kit README describes a broad toolkit with:

- 20 specialized agents
- 36 skills
- 11 workflows

Codex Workflows is adapted to Codex skill mechanics and repository-local `.agent` integration.

## What Antigravity does strongly

- Rich specialist catalog (agents, skills, workflows)
- Strong orchestration concepts
- Command-driven workflow style
- Large knowledge surface for many domains

## Previous gap in this repository

Before this refactor, `codex-workflows` had:

- 1 skill
- 1 compact playbook file
- no automation scripts
- no local template scaffolding

## Refactor outcomes in this repository

Now includes:

- structured per-workflow references
- routing matrix and orchestration gates
- deterministic and fast router variants
- local `.agent` bootstrap script
- reusable `.agent` template bundle
- compatibility manifest and drift checks
- workflow parity checks
- CI validation and unit tests
- codex-native domain packs (backend/frontend/security/qa)
- explicit architecture docs

## Practical difference now

Antigravity-like robustness is approximated by combining:

- a strong router skill
- codified workflow knowledge base
- automation scripts
- project-level template scaffolding
- full compatibility pack mirroring `.agent` structure (`packs/antigravity-compat/.agent`)
- scriptable sync path for future updates (`scripts/sync_compat_pack.py`)

This keeps compatibility with Codex while preserving the workflow mindset.

## Codex-native default track

Bootstrap now defaults to:

`bootstrap_project_agent.py --profile codex-native`

This profile boots from an independent codex-native template root:

- `skills/codex-workflows/templates/codex-native/.agent`
- with all 11 rewritten workflow definitions in `workflows/*.md`
- with native specialist agents in `agents/*.md`
- with native capability skills in `skills/*/SKILL.md`
- `antigravity-compat` remains opt-in interoperability mode.

Quality is enforced by:

- `skills/codex-workflows/scripts/check_codex_native_quality.py`
- `skills/codex-workflows/scripts/check_codex_native_assets.py`
- CI execution in `.github/workflows/ci.yml`
- similarity threshold guard (`--max-similarity 0.35`) versus compatibility workflows.

References are now codex-native aligned:

- `skills/codex-workflows/references/workflows/*.md`
- byte-parity with `templates/codex-native/.agent/workflows/*.md`
- explicitly separated from compatibility parity checks.

## Compatibility Mode

For near-equivalent structure to Antigravity projects, bootstrap with:

`bootstrap_project_agent.py --profile antigravity-compat`

This installs a complete `.agent` tree including agents, skills, workflows, rules, scripts, and shared assets.

Compatibility parity is maintained between:

- `skills/codex-workflows/templates/.agent/workflows/*.md`
- `skills/codex-workflows/packs/antigravity-compat/.agent/workflows/*.md`

## Remaining expansion path

1. Expand codex-native workflow depth with stack-specific execution branches.
2. Add benchmark thresholds and trend tracking for routing/bootstrap latency.
3. Add broader end-to-end sample implementations with automated golden checks.
