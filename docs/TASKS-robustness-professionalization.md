# Tasks: Robustness, Professionalism, Documentation, and Copy-Risk

Date: 2026-02-13
Repository: `D:\Projetos\codex-workflows-skill`
Mode: `/orchestrate`

## Goal

Close the remaining gaps identified in the latest external benchmark comparison while keeping `codex-workflows`:

- technically robust;
- professionally packaged for public adoption;
- fully documented;
- less exposed to "direct copy" perception on the default user path.

## Stage Checklist

- [x] Stage 1: Website multilingual parity (EN/PT/ES/FR/ZH) for source references
- [x] Stage 2: Default profile independence from compatibility pack
- [x] Stage 3: Product-grade unified CLI for install/bootstrap/status/validate/docs sync
- [x] Stage 4: Public governance templates and contributor surface hardening
- [x] Stage 5: Final validation and evidence snapshot

## Stage 1: Website multilingual parity

### Scope

- Expand `website/scripts/sync_reference_docs.py` to sync source docs to all locales (`en`, `pt`, `es`, `fr`, `zh`).
- Make `reference/source.md` pages in all locales point to complete source doc index.
- Ensure locale docs include all source pages:
  - `architecture`
  - `comparison`
  - `workflow-contract`
  - `operations`
  - `release`
  - `robustness-checklist`
  - `compatibility`
  - `performance`

### Acceptance criteria

- Locale parity for source docs is complete (`missing_vs_en_count == 0` for `pt`, `es`, `fr`, `zh`).
- `npm run docs:build` passes.

### Validation commands

- `python website/scripts/sync_reference_docs.py`
- `npm run docs:build` (in `website/`)
- locale parity check script (one-off command in terminal)

## Stage 2: Default profile independence from compatibility pack

### Scope

- Make `codex-native` bootstrap independent from `packs/antigravity-compat`.
- Keep `antigravity-compat` available as explicit opt-in profile.
- Add codex-native core `.agent` assets (architecture/rules/scripts/workflows) inside `templates/codex-native/.agent`.
- Add quality checks and tests that guarantee default path does not require compatibility pack files.

### Acceptance criteria

- `bootstrap_project_agent.py --profile codex-native` does not source `packs/antigravity-compat/.agent`.
- Existing checks and tests pass.
- Docs explain compatibility as optional path.

### Validation commands

- `python skills/codex-workflows/scripts/check_codex_native_quality.py ...`
- `python -m unittest discover -s tests -p "test_*.py"`

## Stage 3: Product-grade unified CLI

### Scope

- Add a root unified CLI entrypoint for maintainers and users:
  - `init` (bootstrap)
  - `status` (health snapshot)
  - `validate` (core checks)
  - `docs-sync` (source docs mirror)
- Ensure cross-platform usage through Python.
- Document CLI in root docs and website docs across all locales.

### Acceptance criteria

- CLI command help works.
- CLI subcommands run successfully in local repository.
- Docs updated in `README.md`, `docs/OPERATIONS.md`, and website locale pages.

### Validation commands

- `python scripts/codexwf.py --help`
- `python scripts/codexwf.py status`
- `python scripts/codexwf.py validate`

## Stage 4: Public governance hardening

### Scope

- Add public collaboration templates under `.github/`:
  - bug report
  - feature request
  - pull request template
- Add or update community/contribution guidance docs.
- Mirror relevant guidance in website docs pages.

### Acceptance criteria

- Templates exist and are valid markdown/yaml.
- Docs reference contribution and issue flow clearly.

### Validation commands

- file presence check in `.github/`
- `npm run docs:build`

## Stage 5: Final validation and evidence

### Scope

- Run complete checks.
- Update this task file with completion marks and evidence.
- Confirm all docs and website locales are in sync.

### Acceptance criteria

- all stages checked as done;
- all validations pass;
- working tree reflects intended modifications only.

### Validation commands

- `python skills/codex-workflows/scripts/check_workflow_parity.py ...`
- `python skills/codex-workflows/scripts/check_codex_native_quality.py ...`
- `python -m unittest discover -s tests -p "test_*.py"`
- `python website/scripts/sync_reference_docs.py`
- `npm run docs:build` (in `website/`)

## Execution Log

- Stage 1 completed:
  - Updated `website/scripts/sync_reference_docs.py` to sync EN/PT/ES/FR/ZH.
  - Updated locale source index pages in:
    - `website/docs/es/reference/source.md`
    - `website/docs/fr/reference/source.md`
    - `website/docs/zh/reference/source.md`
  - Validation:
    - locale parity check result: `en_count=19`, all locales `missing=0`.
    - `npm run docs:build` passed.
- Stage 2 completed:
  - `codex-native` now boots from `templates/codex-native/.agent` only.
  - Added codex-native core files:
    - `ARCHITECTURE.md`
    - `rules/CODEX.md`
    - `scripts/auto_preview.py`
  - Updated docs and website text to position `antigravity-compat` as opt-in.
  - Validation:
    - `check_codex_native_quality.py` passed.
    - `python -m unittest tests.test_bootstrap_profiles` passed.
    - full test suite (`23 tests`) passed.
- Stage 3 completed:
  - Added unified CLI: `scripts/codexwf.py`.
  - Added CLI test coverage: `tests/test_codexwf_cli.py`.
  - Updated root docs and website docs (EN/PT/ES/FR/ZH) with CLI usage.
  - Validation:
    - `python scripts/codexwf.py --help` passed.
    - `python scripts/codexwf.py status --json` passed.
    - `python scripts/codexwf.py validate --tests` passed.
    - `python scripts/codexwf.py docs-sync --build` passed.
- Stage 4 completed:
  - Added public governance templates:
    - `.github/ISSUE_TEMPLATE/bug_report.yml`
    - `.github/ISSUE_TEMPLATE/feature_request.yml`
    - `.github/ISSUE_TEMPLATE/config.yml`
    - `.github/PULL_REQUEST_TEMPLATE.md`
    - `.github/CODEOWNERS`
  - Added governance docs:
    - `docs/COMMUNITY.md`
    - `website/docs/reference/community.md`
    - `website/docs/pt/reference/community.md`
    - `website/docs/es/reference/community.md`
    - `website/docs/fr/reference/community.md`
    - `website/docs/zh/reference/community.md`
  - Validation:
    - governance templates detected in `.github/`.
    - docs locale parity status: `en_count=21`, all locales `missing=0`.
    - `npm run docs:build` passed.
- Stage 5 completed:
  - Final validation commands passed:
    - `check_workflow_parity.py`
    - `check_codex_native_quality.py`
    - `scripts/ci_validate_skill.py --skills-root skills`
    - `python -m unittest discover -s tests -p "test_*.py"` (`25 tests`)
    - `python scripts/codexwf.py status --json` (locale parity confirmed)
    - `python scripts/codexwf.py docs-sync --build`
  - Final locale parity snapshot:
    - `en_count=21`
    - `pt/es/fr/zh` all `count=21`, `missing=0`
