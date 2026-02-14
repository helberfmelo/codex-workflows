# Why Use `cw` in GPT Codex + VS Code

Yes, this is usual for a serious GitHub project website.

A documentation portal should explain:

- what problem the project solves;
- where it adds clear value;
- when it is not necessary.

This page does exactly that, without synthetic metrics.

## Problem `cw` Solves

Without an operating model, Codex usage in large projects often suffers from:

- inconsistent prompt quality between contributors;
- weak handoff between planning, implementation, and validation;
- missing release and governance steps under delivery pressure;
- repeated setup effort across repositories.

## What `cw` Adds

`cw` adds a repeatable execution model on top of Codex:

- explicit workflow activation (`cw /orchestrate`, `cw /debug`, etc.);
- codex-native contracts for workflow behavior;
- domain and stack validation packs (Node, Python, Rust);
- CI and release automation aligned with repository operations;
- multilingual docs and operational playbooks.

## Comparison: With vs Without `cw`

| Dimension | Without `cw` | With `cw` |
| --- | --- | --- |
| Task kickoff | Prompt style varies by person | Explicit workflow trigger and intent |
| Multi-domain work | Coordination is ad hoc | `/orchestrate` with structured phases |
| Validation discipline | Easy to skip checks | Built-in validation routines and CI gates |
| Release hygiene | Manual and error-prone | Automated release/tag/changelog flow |
| Onboarding | Knowledge spread across chat history | Centralized docs, examples, and commands |
| Repeatability | Depends on individual memory | Repository-level conventions and checks |

## When `cw` Is Not Required

For very small one-off tasks, using plain Codex prompts can be enough.

`cw` becomes valuable when you need:

- consistency across contributors;
- auditable quality gates;
- scalable operations and release discipline.

## Practical Recommendation

Use a mixed model:

1. Simple tasks: direct prompts.
2. Product work: `cw` workflows + validation gates.
3. Release cycles: automated checks and release pipeline.
