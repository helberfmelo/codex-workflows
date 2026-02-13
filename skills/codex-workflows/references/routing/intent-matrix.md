# Intent Matrix

Map request intent to a primary workflow.

| Intent Signals | Primary | Secondary | Notes |
|---|---|---|---|
| ideate, options, alternatives | /brainstorm | /plan | Prefer breadth first |
| roadmap, scope, milestones | /plan | /orchestrate | Planning only if requested |
| build from scratch, new app | /create | /orchestrate | For broad builds, ask constraints |
| extend existing feature | /enhance | /test | Keep diffs targeted |
| error, bug, regression, failing | /debug | /test | Root cause before fixes |
| generate tests, coverage gaps | /test | /debug | Include edge cases |
| release, production, rollback | /deploy | /test | Gate on pre-flight checks |
| run locally, start server | /preview | /status | Report health and URL |
| what is done, progress, board | /status | /plan | Show completed/pending |
| complex, multi-domain, end-to-end | /orchestrate | /plan | Require phase gates |
| design system, visual direction | /ui-ux-pro-max | /enhance | Include accessibility checks |

## Confidence Guide

- High: clear keywords and single domain.
- Medium: mixed signals or two close domains.
- Low: vague objective, missing constraints.
