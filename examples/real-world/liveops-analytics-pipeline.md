# Real-World Blueprint: LiveOps Analytics Pipeline

## Target Outcome

Build a production analytics pipeline for game live operations:

- ingest gameplay and economy events;
- aggregate health metrics and anomaly indicators;
- provide operational dashboards and alerting.

## Constraints

- high-throughput ingestion;
- schema evolution safety;
- backfill and replay support;
- privacy and retention controls.

## Recommended Workflow Sequence

1. `/orchestrate`
- align gameplay, backend, data, and security constraints.

2. `/game-dev`
- define event taxonomy and gameplay signal relevance.

3. `/create`
- implement ingestion, validation, and aggregation components.

4. `/enhance`
- tune performance and storage strategy.

5. `/deploy`
- release with monitoring, SLOs, and rollback.

## Suggested Prompt Pack

`cw /orchestrate plan a liveops analytics pipeline for game telemetry with replay support and anomaly detection.`

`cw /game-dev define the event schema and gameplay KPIs that should drive balancing decisions.`

`cw /enhance optimize ingestion throughput and reduce processing latency under burst traffic.`

## Acceptance Gates

- schema compatibility checks in place;
- replay and backfill procedure documented;
- alert thresholds defined and validated;
- release and incident response runbooks approved.
