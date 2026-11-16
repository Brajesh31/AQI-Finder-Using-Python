# 🆘 Support and troubleshooting

## Before opening a support request

1. Read the [README](README.md).
2. Follow the [installation guide](docs/installation.md).
3. Check [troubleshooting](docs/troubleshooting.md).
4. Confirm that the intended Python interpreter has Requests and Tkinter available.
5. Confirm that `WAQI_TOKEN` is configured in the same terminal/session used to launch the program.

## What to include

A useful report includes:

- operating system and version;
- Python version;
- Requests version;
- whether Tkinter imports successfully;
- the exact command used to launch the app;
- the general type of query (a city or station name, sanitized where necessary);
- the visible status/error message;
- steps to reproduce;
- whether the issue happens consistently or intermittently.

## What not to include

Never include a real WAQI token, a credential-bearing URL, personal precise location, private search history, or unredacted logs containing secrets. Do not publish screenshots that expose API keys or private user information.

## Provider-specific issues

The application depends on the external WAQI service. Service availability, quota, supported station names, provider response fields, and data freshness are outside this repository's control. Check the provider's current documentation and service status before assuming an application defect.

A missing AQI response does not mean that air quality is good.

## Reporting a bug

Use the repository's bug report issue template when available. Include a minimal reproduction and explain expected versus actual behaviour. For security issues, use the private route in [SECURITY.md](SECURITY.md), not a public issue.

## Scope

This repository is a small desktop project maintained on a best-effort basis. Support does not imply continuous monitoring, guaranteed response time, medical advice, or provider support.
