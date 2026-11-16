# 🚀 Installation and local setup

## 1. Prerequisites

- Python 3.10 or newer is recommended for the type-annotated application code.
- Tkinter must be available in the Python installation.
- Internet access is required for a live WAQI lookup.
- A valid WAQI token is required and must be supplied through the `WAQI_TOKEN` environment variable.
- Git is optional if downloading the repository ZIP instead of cloning it.

## 2. Clone the repository

```bash
git clone https://github.com/Brajesh31/AQI-Finder-Using-Python.git
cd AQI-Finder-Using-Python
```

## 3. Create an isolated environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\\Scripts\\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

## 4. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Tkinter is usually included with standard Windows and macOS Python distributions. On many Debian/Ubuntu-based Linux installations it is supplied separately by the operating system package `python3-tk`. Install the package matching the Python interpreter you intend to use. Do not try to install Tkinter using pip.

## 5. Configure the WAQI token

Create a local `.env` file by copying the safe template and replacing the placeholder with your own token. The application itself reads environment variables and does not automatically parse `.env`, so export the variable in your shell before running.

PowerShell:

```powershell
$env:WAQI_TOKEN = "your-waqi-token"
python "AQI PYTHON"
```

Windows Command Prompt:

```cmd
set WAQI_TOKEN=your-waqi-token
python "AQI PYTHON"
```

macOS/Linux:

```bash
export WAQI_TOKEN="your-waqi-token"
python "AQI PYTHON"
```

Never commit `.env` or a real token. The original source contained a hard-coded token. Treat that value as compromised and rotate it with the provider. See [Security policy](../SECURITY.md).

## 6. Launch the application

```bash
python "AQI PYTHON"
```

Enter a city or station query supported by WAQI and select **Find AQI**. The interface displays a loading state while the request runs. The provider may return a station-specific measurement rather than a city-wide average.

## 7. Verify your environment

```bash
python --version
python -m pip show requests
python -c "import tkinter; print('Tkinter available')"
```

A graphical desktop session is required. A headless CI runner generally cannot open the application window, so use unit tests and mocked API responses in CI rather than launching the GUI there.
