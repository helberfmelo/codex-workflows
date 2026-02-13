# E2E Example: Node Auth API

## Scenario

Build a production-grade auth API for a SaaS admin panel:

- email/password + JWT refresh flow;
- role-based authorization (`admin`, `editor`, `viewer`);
- audit logging and rate limit;
- OpenAPI docs and CI checks.

## Prompt Sequence

1. Discovery and planning:

`Use codex-workflows in /orchestrate and design a Node.js + TypeScript auth API for a SaaS admin panel, including architecture, threat model, and test strategy.`

2. Implementation:

`Continue with codex-workflows /orchestrate and implement phase 1 (domain models, auth modules, migration scripts).`

3. Hardening:

`Use codex-workflows in /enhance to add security hardening (rate limit, token rotation, audit trail) and update tests.`

4. Release readiness:

`Use codex-workflows in /deploy and produce release checklist, rollback plan, and CI gates.`

## Expected Deliverables

- API modules for auth/session/roles
- migration files and seed data
- unit/integration tests for auth and authorization
- deployment checklist with rollback
- concise orchestration report

## Validation Commands

`python skills/codex-node-validation-pack/scripts/validate_node_stack.py --project .`

`python skills/codex-node-validation-pack/scripts/validate_node_stack.py --project . --run`
