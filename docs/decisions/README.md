# 🧠 Architecture decision records

Architecture decision records (ADRs) preserve the reasoning behind choices that affect maintainability, security, privacy, or interpretation of AQI observations.

## When to add an ADR

Create a record when deciding to change provider, add another AQI standard, store observations, introduce a remote service, collect location information, add notifications, or package the app with a credential/configuration mechanism. Routine formatting changes do not need an ADR.

## Status vocabulary

- **Proposed:** under discussion, not approved for implementation.
- **Accepted:** chosen for the current architecture or planned work.
- **Deprecated:** no longer recommended but retained for context.
- **Superseded:** replaced by a later decision.

Use [the ADR template](../templates/architecture-decision-record.md). Include context, alternatives, rationale, consequences, security/privacy impact, and validation criteria.

## Current decisions

### ADR-0001: Keep the application desktop-first

Status: Accepted.

Context: The current feature is an on-demand local lookup. A hosted service adds infrastructure, uptime, monitoring, credential storage, and privacy responsibilities.

Decision: Keep the current product as a local Tkinter program unless a concrete multi-user requirement justifies a different architecture.

Consequences: Users install locally and configure their own provider token. There is no central history or server-side cache.

### ADR-0002: Do not persist queries by default

Status: Accepted.

Context: Location and search history can reveal sensitive behavioural information.

Decision: The app does not store lookup history by default.

Consequences: The program is stateless between launches. A future history feature must define consent, storage, retention, and deletion.

### ADR-0003: Treat the AQI mapping as project-specific

Status: Accepted.

Context: AQI standards differ across jurisdictions.

Decision: Preserve the original six thresholds but document that they are not universal.

Consequences: Any new national index needs its own methodology, tests, source reference, and explicit UI label.
