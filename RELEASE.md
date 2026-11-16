# 🚀 Release process

## Release readiness

Before creating a release:

1. Review the current README, roadmap, and changelog.
2. Confirm no real WAQI token is present in tracked files or recent changes.
3. Confirm any previously committed token has been revoked or rotated.
4. Install dependencies in a clean environment.
5. Run `python -m pytest` and record the result.
6. Manually launch the GUI on the target operating systems.
7. Verify success, unavailable query, timeout, and malformed-response behaviour.
8. Confirm the AQI standard and health wording are described conservatively.
9. Check WAQI terms, attribution, and quota requirements.
10. Update release notes and documentation.

## Versioning

Use semantic versioning when formal releases are adopted. A patch release fixes defects without changing public behaviour. A minor release adds compatible functionality. A major release signals a breaking change or substantial redesign. Do not create a version tag until the release criteria have evidence.

## Release notes

Document user-visible changes, configuration changes, tested Python and OS environments, dependency changes, known limitations, and migration instructions. Never include credentials or private location data.

## Rollback

If a release exposes a credential, misrepresents AQI categories, or breaks core lookup behaviour, withdraw or supersede the release. Rotate exposed credentials with the provider. Publish the corrected version and state known impact without reproducing secrets.
