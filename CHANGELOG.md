# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog and this project follows Semantic Versioning.

## [Unreleased]

### Added

- Skill upgrade to workflow operating system model.
- Routing matrix and orchestration phase gate references.
- Per-workflow knowledge files under `references/workflows/`.
- Output report templates for standard and orchestration flows.
- `route_workflow.py` deterministic workflow classifier.
- `bootstrap_project_agent.py` to scaffold `.agent` into any project.
- Built-in `.agent` templates with workflows, rules, and architecture.
- `docs/ARCHITECTURE.md` and `docs/COMPARISON.md`.

## [1.0.0] - 2026-02-13

### Added

- Initial public release of `codex-workflows` skill.
- Workflow routing for `/brainstorm`, `/plan`, `/create`, `/enhance`, `/debug`, `/test`, `/deploy`, `/preview`, `/status`, `/orchestrate`, and `/ui-ux-pro-max`.
- Skill metadata in `agents/openai.yaml`.
- Workflow reference playbook in `references/workflow-playbook.md`.
- Installation and usage documentation.
