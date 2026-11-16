# 🧰 Troubleshooting guide

## `ModuleNotFoundError: No module named 'requests'`

Activate the intended virtual environment and install the dependency:

```bash
python -m pip install -r requirements.txt
python -m pip show requests
```

Confirm that the interpreter used to run the app is the same interpreter where Requests was installed.

## Tkinter cannot be imported

Tkinter is commonly bundled with standard Python installers, but Linux distributions may package it separately. On Debian/Ubuntu-based systems, install the matching `python3-tk` system package. Do not try `pip install tkinter`. Verify with:

```bash
python -c "import tkinter; print('Tkinter available')"
```

## `WAQI_TOKEN` missing

The application reads the token from the process environment. Configure it in the same terminal/session used to launch the app.

PowerShell:

```powershell
$env:WAQI_TOKEN = "your-token"
python "AQI PYTHON"
```

macOS/Linux:

```bash
export WAQI_TOKEN="your-token"
python "AQI PYTHON"
```

Do not paste a real token into an issue or screenshot. If a token was previously committed, revoke or rotate it with WAQI.

## No AQI data returned

Check query spelling, provider availability, token validity, and whether the feed supports the query. Some names may resolve to multiple stations or not resolve as expected. A missing reading does not mean the air is clean.

## Timeout or connection failure

Check network access and provider status. The client uses a finite timeout. Retry later rather than creating a rapid request loop. DNS, firewall, proxy, or provider outages can also block access.

## Window freezes during lookup

Network requests should run on the worker thread, while widget updates are scheduled on the Tkinter main loop. Do not call Tk widget methods directly from a worker thread. For multiple simultaneous requests, track request identity and discard stale responses deliberately.

## Station or timestamp metadata is blank

The provider may omit optional fields. Show only metadata actually received. Do not substitute the computer's current time as the observation time.

## Category differs from another AQI app

Providers and jurisdictions can use different AQI calculations and breakpoints. This app preserves its own six-category mapping. Compare index method, station, pollutant coverage, and observation time before judging a discrepancy.

## GUI does not open in CI

A headless runner usually has no graphical display. Run unit and mocked API tests in CI. Test the Tkinter window manually or with a deliberately configured virtual display.
