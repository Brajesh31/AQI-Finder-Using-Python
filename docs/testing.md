# 🧪 Testing strategy

## 1. Objectives

Tests should verify the behaviour the project owns without depending on a live WAQI service, consuming provider quota, requiring an API token, or launching a visible desktop window in CI.

The most important deterministic behaviour is the AQI category mapping and the handling of successful, unavailable, malformed, and failed provider responses. UI smoke tests should verify interaction wiring separately from provider communication.

## 2. Test layers

| Layer | What to verify | External dependency |
|---|---|---|
| Unit | AQI category boundaries and invalid values | None |
| Provider client | URL/query construction, timeout, HTTP status, JSON and schema checks | Mocked Requests session |
| Application logic | Empty city and missing token handling | Mocked provider client |
| UI | Loading, success, failure, disabled button, result formatting | Tk display or controlled UI test harness |
| Manual smoke | Window opens, keyboard entry works, and result display is legible | Desktop OS and optional valid token |

## 3. Boundary test matrix

Test each transition around the configured thresholds. For example, values 50 and 51 must map to different categories; likewise 100/101, 150/151, 200/201, and 300/301. Test zero, decimal numbers if supported, very large values, negative numbers, booleans, strings, and missing values.

## 4. Provider response fixtures

Use synthetic responses for at least:

- successful payload with AQI and all optional metadata;
- successful payload without station name;
- successful payload without observation timestamp;
- provider status other than `ok`;
- missing `data` object;
- missing AQI;
- negative, boolean, string, or null AQI;
- invalid JSON;
- HTTP 4xx and 5xx;
- connection failure;
- timeout.

Never use a real key in fixtures. The CI workflow must not call the live WAQI service.

## 5. Manual GUI checklist

- [ ] The application opens without a traceback.
- [ ] The window has a useful title and a sensible minimum size.
- [ ] Empty input produces actionable feedback.
- [ ] Missing token produces configuration guidance.
- [ ] The search button is disabled while a request is in progress.
- [ ] The interface remains responsive during the request.
- [ ] Successful results show AQI, category, and optional provider metadata.
- [ ] A failure restores the search button.
- [ ] Keyboard Enter can start a search.
- [ ] Text is readable at common display scaling settings.

## 6. Run tests

Install development dependencies with:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest
```

The test suite should use dependency injection or mocks for all network paths. Do not make tests depend on a current station's exact reading because live values change.

## 7. Evidence and release gate

A passing test suite demonstrates only the conditions covered by those tests. Record Python version, operating system, test command, number of tests, and manual GUI platforms checked. Do not claim cross-platform compatibility from a single developer machine.
