# 📝 Changelog

All notable user-facing changes to AQI Finder Using Python are recorded here. Entries should describe changes that actually landed in the repository. Planned work belongs in [ROADMAP.md](ROADMAP.md), not in a release history.

The project began as a small Tkinter prototype that queried the WAQI feed and mapped the returned AQI number to six display categories.

## [Unreleased]

### Added
- Detailed architecture, API, AQI methodology, installation, testing, accessibility, deployment, persistence, and troubleshooting documentation.
- Mermaid component and request-flow diagrams.
- Reusable ADR, test-plan, and incident-report templates.
- Repository contribution, support, and security guidance.

### Changed
- WAQI token is now loaded from the `WAQI_TOKEN` environment variable instead of being embedded in application source.
- Provider calls now use finite timeouts and explicit response validation.
- Network lookups are performed outside the Tkinter event loop, with UI callbacks scheduled on the main thread.
- User-facing errors are safer and avoid exposing raw request details.
- Optional station and observation-time metadata is displayed when returned.

### Security
- The previously committed provider token is treated as exposed and should be rotated with WAQI. Replacing the current source value does not remove historical Git objects.

### Validation status
- Automated test coverage is a planned follow-up and must not be represented as passing until tests are committed and run.
- Live provider behaviour and current station selector/query coverage have not been exhaustively verified.

## [0.1.0] - 2025-01-01

### Added
- Initial Tkinter AQI lookup prototype.
- City query using the WAQI feed.
- Six-level AQI display mapping.

Date and version information for this initial entry reflects the project's existing changelog metadata; verify release tags before using it as formal release evidence.
