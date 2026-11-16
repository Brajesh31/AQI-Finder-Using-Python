# Test plan: <change or release>

## Scope

Describe the behaviours changed and the behaviours intentionally not changed.

## Environment

| Field | Value |
|---|---|
| Python version | |
| Operating system | |
| Tkinter availability | |
| Requests version | |
| Commit SHA | |

## Unit and provider tests

| Case | Input or fixture | Expected result | Actual result | Status |
|---|---|---|---|---|
| Lower AQI boundary | | | | |
| Upper AQI boundary | | | | |
| Invalid AQI | | | | |
| Provider failure | | | | |
| Malformed response | | | | |

## Manual UI tests

- [ ] Application opens.
- [ ] Empty input is handled.
- [ ] Missing token is handled.
- [ ] Loading state is visible.
- [ ] Success result is readable.
- [ ] Error path restores controls.
- [ ] Keyboard-only flow works.
- [ ] Resizing and display scaling are acceptable.

## Security and privacy checks

- [ ] No real token appears in diff, logs, or screenshots.
- [ ] Token is supplied from environment configuration.
- [ ] No unnecessary user location is stored.
- [ ] Network errors do not leak credential-bearing URLs.

## Results and limitations

Summarize what passed, what failed, what was not tested, and whether the change is ready for release.
