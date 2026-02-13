# Community and Governance

`codex-workflows` is maintained as a public project with explicit contribution workflows.

## Issue templates

- Bug report: `.github/ISSUE_TEMPLATE/bug_report.yml`
- Feature request: `.github/ISSUE_TEMPLATE/feature_request.yml`
- Issue config: `.github/ISSUE_TEMPLATE/config.yml`

## Pull requests

- Template: `.github/PULL_REQUEST_TEMPLATE.md`
- Ownership rules: `.github/CODEOWNERS`

## Contributor flow

1. Open an issue with reproducible context.
2. Align acceptance criteria.
3. Implement in small, traceable changes.
4. Run validations before opening PR.

Recommended validation:

`python scripts/codexwf.py validate --tests --docs`
