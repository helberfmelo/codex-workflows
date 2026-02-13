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
- deterministic router script
- local `.agent` bootstrap script
- reusable `.agent` template bundle
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

## Compatibility Mode

For near-equivalent structure to Antigravity projects, bootstrap with:

`bootstrap_project_agent.py --profile antigravity-compat`

This installs a complete `.agent` tree including agents, skills, workflows, rules, scripts, and shared assets.

## Next expansion path

1. Add domain packs (`backend`, `frontend`, `security`, `qa`) as additional skills.
2. Add verification scripts per stack (Node, Python, Rust).
3. Add richer status and session management scripts.
4. Add examples folder with real project walkthroughs.
