# E2E Example: FastAPI Orders Service

## Scenario

Build an orders microservice for an e-commerce platform:

- FastAPI + async SQLAlchemy;
- idempotent order creation endpoint;
- webhook ingestion with signature verification;
- contract tests and deployment health checks.

## Prompt Sequence

1. Architecture and plan:

`Use codex-workflows em /orchestrate e planeje um serviço FastAPI de pedidos com idempotência, filas de eventos e monitoramento operacional.`

2. Core implementation:

`Continue with codex-workflows /create and implement the API skeleton, repository layer, and validation models.`

3. Quality and reliability:

`Use codex-workflows in /test to generate integration and contract tests for order creation, retries, and webhook verification.`

4. Operations:

`Use codex-workflows in /status and produce readiness matrix (tests, migrations, observability, release risks).`

## Expected Deliverables

- FastAPI endpoints and service layer
- database schema/migrations
- idempotency and webhook verification logic
- test suite with happy and failure-path coverage
- readiness matrix with release blockers

## Validation Commands

`python skills/codex-python-validation-pack/scripts/validate_python_stack.py --project .`

`python skills/codex-python-validation-pack/scripts/validate_python_stack.py --project . --run`
