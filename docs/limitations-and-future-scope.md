# ⚠️ Limitations and future scope

## 1. Current limitations

### Data and provider coverage

- A city query may resolve to a monitoring station rather than a city-wide aggregate.
- Station availability, sensor status, pollutant coverage, and update cadence are provider-dependent.
- Provider failures, token quota, network connectivity, and response schema changes can prevent a lookup.
- A missing reading must not be interpreted as clean air.

### AQI interpretation

- The project preserves the original six category breakpoints.
- AQI calculations and health categories vary across jurisdictions.
- The application does not independently calculate AQI from pollutant concentrations.
- The output is informational and does not replace official public-health alerts or medical advice.

### Application behaviour

- The project is a local desktop application, not a hosted web service.
- It has no database, login, user profile, search history, or scheduled alerts.
- It does not automatically detect the user's location.
- There is no offline cache or historical chart.
- A valid WAQI token is required for provider access.

## 2. Prioritized roadmap

### Phase 1: Reliability and security

- [x] Move the token out of source code into environment configuration.
- [x] Add finite request timeout and provider error handling.
- [x] Validate the response before presenting a value.
- [x] Keep network work off the Tkinter event loop.
- [ ] Add automated unit tests and mocked provider tests.
- [ ] Confirm historical committed token is revoked.

### Phase 2: Better interpretation

- [ ] State the precise AQI system and jurisdiction represented by the displayed category table.
- [ ] Add a transparent index-method selection only after implementing and validating each method.
- [ ] Improve station context and make observation timestamps explicit.
- [ ] Document provider attribution and usage terms.

### Phase 3: User experience

- [ ] Add loading animation or progress indicator only if it improves the experience.
- [ ] Add retry control with a sensible backoff policy.
- [ ] Improve keyboard and screen-reader support across target systems.
- [ ] Add optional manual station selection where provider support allows it.

### Phase 4: Optional capabilities

- [ ] Consider charts only after a valid historical data source and retention policy exist.
- [ ] Consider local history only with an explicit privacy decision and user control.
- [ ] Consider alerts only with a reliable refresh schedule, consent, and clear failure behaviour.
- [ ] Consider packaged desktop builds after testing on each target operating system.

## 3. Do not add features without a requirement

A database, server, login system, location tracking, and always-on notifications would add complexity and privacy obligations. They are not automatically improvements for a small on-demand desktop lookup. Prioritize correctness, transparent AQI interpretation, and resilience first.

## 4. Definition of done

A roadmap item is complete only when its implementation exists, tests cover expected and failure paths, documentation is updated, and the project no longer describes the feature as proposed. A checked box should never be used as a substitute for validation evidence.
