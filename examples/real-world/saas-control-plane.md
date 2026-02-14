# Real-World Blueprint: SaaS Control Plane

## Target Outcome

Build a multi-tenant control plane covering:

- identity and access;
- organizations and billing;
- auditability and admin operations.

## Constraints

- strict tenant isolation;
- SOC2-friendly audit trails;
- zero-downtime migration path from legacy auth;
- release cadence every 2 weeks.

## Recommended Workflow Sequence

1. `/orchestrate`
- define architecture, risk map, and phase gates.

2. `/plan`
- create roadmap with service boundaries and dependencies.

3. `/create`
- implement foundational services (auth, org, billing contract).

4. `/enhance`
- add resiliency, observability, and operational tooling.

5. `/test`
- harden integration, contract, and failure-path tests.

6. `/deploy`
- produce release package, rollback, and post-release checks.

## Suggested Prompt Pack

`cw /orchestrate design a SaaS control plane with tenant isolation, role hierarchy, and auditable admin actions.`

`cw /plan break this into 4 milestones with acceptance gates and rollback constraints.`

`cw /create implement milestone 1 with migration-safe contracts and tests.`

## Acceptance Gates

- tenant boundary tests passing;
- audit logging coverage for admin actions;
- deployment and rollback runbook validated;
- blocker list closed or explicitly accepted.
