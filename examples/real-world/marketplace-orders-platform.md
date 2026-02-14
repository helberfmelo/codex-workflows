# Real-World Blueprint: Marketplace Orders Platform

## Target Outcome

Deliver a resilient order platform for a multi-vendor marketplace with:

- checkout orchestration;
- payment and fulfillment integration;
- order lifecycle tracking and dispute flow.

## Constraints

- idempotent order creation;
- external provider retries and compensation;
- strict SLA on order status consistency;
- traceability for support and finance teams.

## Recommended Workflow Sequence

1. `/orchestrate`
- model domain boundaries and reliability risks.

2. `/create`
- implement order API, persistence model, and event contracts.

3. `/debug`
- isolate race conditions and retry edge cases.

4. `/test`
- produce integration + contract + replay tests.

5. `/status`
- summarize readiness and unresolved risks.

## Suggested Prompt Pack

`cw /orchestrate define architecture for a multi-vendor marketplace orders platform with idempotency and event-driven fulfillment.`

`cw /create implement order creation contract, persistence, and event publishing interface.`

`cw /test add reliability tests for retries, duplicate submissions, and partial provider outages.`

## Acceptance Gates

- duplicate order prevention validated;
- provider timeout behavior validated;
- observability checkpoints for each lifecycle state;
- release checklist approved by backend + QA owners.
