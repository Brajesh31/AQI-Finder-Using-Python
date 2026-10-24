# AQI Finder Using Python

A small desktop application that looks up a city's current Air Quality Index (AQI) using Tkinter and the World Air Quality Index (WAQI) feed.

## Current implementation

- `AQI PYTHON` contains the complete application.
- Tkinter provides the desktop UI.
- `requests` calls `https://api.waqi.info`.
- The UI reports the AQI and a six-level label from Good through Hazardous.

## Setup

Use Python 3. Install the runtime dependency:

```bash
python -m pip install requests
python "AQI PYTHON"
```

Tkinter is included with most standard Python installations. On Linux, install the distribution's Tk package if it is missing.

## Configuration and security

The current script contains a hard-coded WAQI token. Treat it as exposed and replace it before publishing or deploying. A follow-up should load `WAQI_TOKEN` from the environment, add request timeouts, validate API responses, and avoid displaying raw exception details.

AQI is informational and not medical advice. Always follow local public-health guidance.

## License

MIT License. See [`LICENSE`](./LICENSE).

Last updated: 2026-10-24 09:54 UTC
