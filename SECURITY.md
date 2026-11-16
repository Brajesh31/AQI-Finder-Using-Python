# 🔐 Security Policy

## Supported versions

Security fixes are applied to the current default branch. This repository is a small desktop application and does not currently publish a formal multi-version support matrix.

## Reporting a vulnerability

Please do not publish API tokens, credentials, private location data, or exploitable details in a public issue. Contact the maintainer through the private contact route available from the GitHub profile [@Brajesh31](https://github.com/Brajesh31). Include the affected file, impact, a minimal sanitized reproduction, and any suggested mitigation.

## Credential exposure response

The original prototype contained a WAQI token directly in the Python source. Any token committed to a public repository must be treated as compromised, even after the code is updated. Revoke or rotate that token with the provider. Environment variables prevent new accidental commits, but do not erase historical Git objects or undo prior exposure.

The application now reads `WAQI_TOKEN` from the process environment. Keep real credentials in an untracked `.env` file or a managed secret store, and never put them in `.env.example`, screenshots, logs, bug reports, or desktop screenshots.

## Data and network safeguards

- Send the provider token only to the configured WAQI HTTPS endpoint.
- Use a finite network timeout and handle provider failures without displaying secrets.
- Do not collect or persist a user's location without a clear need and their awareness.
- Do not add telemetry or location history without a documented privacy decision.
- Do not attempt to bypass provider authentication, quotas, or access controls.
- Avoid logging full request URLs because query strings may contain credentials.

## Maintainer checklist

- [ ] Rotate any historically committed token.
- [ ] Search current source and documentation for credential-like strings.
- [ ] Confirm `.env` is ignored by Git.
- [ ] Confirm error messages do not expose tokens or full request URLs.
- [ ] Review dependency updates and GitHub Actions permissions.
- [ ] Document any incident and its remediation without republishing the secret.
