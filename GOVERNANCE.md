# 🏛️ Project governance

## Stewardship

AQI Finder is maintained as a small open-source desktop project. The maintainer coordinates scope, reviews contributions, and makes release decisions. Contributors are encouraged to discuss substantial changes before implementation.

## Decision principles

1. Correct AQI interpretation takes priority over visual polish.
2. Provider credentials must never be committed or exposed in logs.
3. User location and lookup history should not be collected or stored without a clear need and privacy design.
4. External provider behaviour must be validated and failures communicated safely.
5. Health-related statements must be conservative and linked to authoritative guidance before inclusion.
6. Architecture should remain proportionate to a single-purpose desktop tool.

## Changes requiring discussion

A design discussion or ADR is recommended before adding a provider, a second AQI methodology, persistent history, geolocation, notifications, a backend service, telemetry, or a packaging mechanism that changes secret handling.

## Contribution review

Contributions should explain the problem, implementation approach, tests, user-visible impact, data handling, and documentation changes. No contribution should claim a capability is implemented without working code and validation evidence.

## Releases

A release should identify the source revision, supported Python/OS environments, dependency versions, test evidence, provider requirements, attribution, and known limitations. A release should be withdrawn or corrected when it exposes credentials or materially misrepresents AQI data.
