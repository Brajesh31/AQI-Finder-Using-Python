# 🤝 Contributing to AQI Finder Using Python

Thank you for considering a contribution. The most valuable changes improve reliability, correctness, security, accessibility, and clarity. This is a small desktop application, so changes should remain proportionate to the feature.

## Before starting

1. Read the root README and the relevant guide under `docs/`.
2. Search existing issues to avoid duplicating work.
3. For a large change, open an issue describing the motivation and proposed approach.
4. Confirm that the change does not require exposing provider tokens or collecting unnecessary location information.
5. Keep the current desktop-first scope unless a separate architectural proposal is accepted.

## Development environment

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`. Verify Tkinter separately because it is supplied by the Python/OS distribution, not by this project's pip requirements.

## Branch and commit workflow

Use a focused branch such as `fix/provider-timeout`, `feat/station-context`, or `docs/aqi-methodology`. Keep commits small and descriptive. Do not combine unrelated formatting, refactoring, and feature work into one pull request.

## Implementation standards

- Keep provider access separate from presentation logic where practical.
- Validate external data before indexing into nested objects.
- Use finite network timeouts.
- Do not log credential-bearing URLs or tokens.
- Do not update Tkinter widgets from worker threads.
- Handle missing optional provider metadata without inventing values.
- Keep AQI category boundaries explicit and independently testable.
- Do not describe a station measurement as a guaranteed city-wide average.
- Prefer the standard library and existing dependencies unless a new dependency has clear benefit.

## Testing expectations

Run:

```bash
python -m pytest
```

Add or update tests for changed behaviour. Provider tests should use mocked HTTP sessions and synthetic payloads. Do not depend on live WAQI availability or consume live quota in CI. GUI changes require manual desktop validation on the target operating system.

## Documentation expectations

Update the README and the relevant guide when changing user-visible behaviour, configuration, provider fields, AQI methodology, or installation steps. Update Mermaid diagrams when the runtime flow changes. Label proposals as proposals and do not invent test results, station readings, screenshots, or supported operating systems.

## Pull request checklist

- [ ] The motivation and scope are clear.
- [ ] Existing behaviour and limitations are described accurately.
- [ ] Tests were added or updated.
- [ ] Tests were run and results are reported.
- [ ] UI changes were manually checked where applicable.
- [ ] Provider errors and missing fields are handled.
- [ ] No real token, personal data, or private location history is included.
- [ ] Documentation and diagrams are updated.
- [ ] No unrelated files or generated artefacts were added.

## Data and safety

AQI is an environmental indicator, not a medical diagnosis. Do not add personalized health recommendations without authoritative review. Do not collect precise user location or store search history unless the feature has a documented privacy rationale, user controls, retention policy, and deletion path.
