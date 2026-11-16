# 🛠️ Development guide

## Repository conventions

Keep this small desktop application straightforward. Separate concerns when adding functionality, prefer readable functions with explicit validation, and avoid adding frameworks, databases, or background services without a real use case.

## Current implementation areas

- **UI:** Tkinter window, location entry, search button, and result/status labels.
- **Configuration:** `WAQI_TOKEN` environment variable.
- **Provider access:** Requests call to the WAQI feed with a finite timeout.
- **Validation:** JSON structure, provider status, and non-negative numeric AQI.
- **Classification:** `get_aqi_level` category mapping.
- **Threading:** background worker for network activity and main-thread UI callbacks.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

On Windows PowerShell, use `.venv\\Scripts\\Activate.ps1`. On Linux, install the system Tk package matching the interpreter if it is missing.

## Code quality requirements

- Keep real credentials outside tracked source files.
- Add finite timeouts to external requests.
- Validate responses before reading nested fields.
- Treat booleans separately from numbers when validating measurements.
- Keep Tkinter widget updates on the UI thread.
- Use actionable messages rather than raw tracebacks in the interface.
- Keep AQI breakpoint policy documented and tested.
- Do not present one station result as a guaranteed city-wide average.

## Testing workflow

Run `python -m pytest`. Use mocked sessions and synthetic payloads for provider tests. Do not consume a real WAQI token or live quota in unit tests. Perform GUI smoke testing manually on the desktop systems the project claims to support.

## Pull request expectations

A contribution should include the problem statement, behaviour changes, tests or manual validation evidence, screenshots for UI changes when appropriate, and updated documentation. Mention provider terms, credential handling, and location implications where relevant.

## Suggested code structure if the app grows

```text
src/aqi_finder/
├── __init__.py
├── app.py
├── provider.py
├── classification.py
└── config.py

tests/
├── test_classification.py
├── test_provider.py
└── test_ui_logic.py
```

This is a proposal, not the current tree. Do not reorganize the small application solely to match an example structure.
