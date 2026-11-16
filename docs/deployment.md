# 📦 Packaging and distribution

## Current deployment model

AQI Finder is a local desktop application, not a web server or cloud service. Users run the Python program on a computer with a graphical desktop, compatible Python/Tkinter, Requests, network access, and a valid WAQI token.

## Pre-distribution checks

- [ ] Remove credentials from source and rotate any token ever committed publicly.
- [ ] Review current WAQI terms, quota, and attribution requirements.
- [ ] Install dependencies in a clean environment.
- [ ] Run unit and mocked provider tests.
- [ ] Smoke-test the GUI on every target operating system.
- [ ] Confirm errors do not expose tokens or full request URLs.
- [ ] Document how users obtain and configure their own token.
- [ ] Identify the AQI index method and jurisdiction accurately.
- [ ] Include third-party license and attribution information where required.

## Run from source

```bash
python -m pip install -r requirements.txt
python "AQI PYTHON"
```

Configure `WAQI_TOKEN` in the process environment before launching. See [Installation](installation.md).

## Optional executable packaging

A future Windows executable or macOS/Linux package could use PyInstaller, but no packaging configuration is currently committed. Determine how users provide the token without baking it into the binary. Bundled executables do not make embedded secrets safe. Test on a clean target machine rather than only on the developer environment.

## Platform considerations

- **Windows:** verify Tkinter availability and test PowerShell and Command Prompt configuration.
- **macOS:** verify a compatible Tcl/Tk build and test app launch permissions.
- **Linux:** install the distribution Tk package where needed and test in a graphical desktop session.

A headless CI runner generally cannot open the visible desktop interface. CI should test pure logic and mocked network behaviour instead.

## Release and rollback

Record source commit, Python and dependency versions, operating systems tested, test results, provider configuration instructions, and known limitations. Withdraw a release if it introduces incorrect AQI interpretation, unsafe credential handling, or broken provider access, then publish a corrected build with a clear change note.
