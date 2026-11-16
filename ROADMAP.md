# 🗺️ Project roadmap

This roadmap separates work already present from possible future work. A roadmap checkbox is not proof of completion; close an item only after implementation, tests, documentation, and review.

## Phase 1: Reliability and credential safety

- [x] Move WAQI token out of tracked application source and read `WAQI_TOKEN` from the process environment.
- [x] Add finite request timeout.
- [x] Validate HTTP status, JSON response shape, provider status, and numeric AQI.
- [x] Handle network lookup outside the Tkinter event loop.
- [x] Present safe provider errors without printing request URLs or tokens.
- [ ] Revoke/rotate the historical token that was committed in an earlier version.
- [ ] Add automated tests for every classification boundary and provider failure.
- [ ] Validate the full workflow on clean Windows, macOS, and Linux desktop environments.

## Phase 2: AQI interpretation

- [ ] Identify and document the precise index standard and jurisdiction represented by the current six breakpoints.
- [ ] Review category text against an authoritative source before presenting public-health claims.
- [ ] Add separate, tested classification tables only if the project explicitly supports multiple standards.
- [ ] Display provider station and observation-time provenance consistently.
- [ ] Document how missing, stale, and invalid provider readings are represented.

## Phase 3: Desktop usability

- [ ] Test keyboard-only interaction and assistive-technology compatibility.
- [ ] Review scaling, window resizing, and long station/category text.
- [ ] Add a retry action only with sensible request throttling.
- [ ] Improve station disambiguation if the provider supports it.
- [ ] Capture screenshots from a real running application, with no private token or personal data visible.

## Phase 4: Distribution

- [ ] Select target operating systems.
- [ ] Evaluate executable packaging and safe user-managed token configuration.
- [ ] Test packaged builds on clean machines.
- [ ] Document provider terms, attribution, update procedure, and known limitations.

## Phase 5: Optional features, only when justified

- [ ] Consider local observation history with a documented privacy and deletion design.
- [ ] Consider trends only when observations have consistent station, time, and index-method provenance.
- [ ] Consider notifications only with reliable refresh behaviour and explicit user consent.
- [ ] Consider a backend only if a concrete multi-user requirement justifies its infrastructure and security costs.

## Explicit non-goals for the current release

- Medical diagnosis or personalized clinical advice.
- Guaranteed emergency alerts.
- A claim that one station represents an entire city.
- Automatic location tracking or collection of location history.
