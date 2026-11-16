import importlib.util
from pathlib import Path

import pytest
import requests

APP_PATH = Path(__file__).resolve().parents[1] / "AQI PYTHON"
spec = importlib.util.spec_from_file_location("aqi_app_provider", APP_PATH)
app = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(app)

class FakeResponse:
    def __init__(self, payload, status_code=200):
        self.payload = payload
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError("HTTP failure")

    def json(self):
        if isinstance(self.payload, Exception):
            raise self.payload
        return self.payload

class FakeSession:
    def __init__(self, response=None, error=None):
        self.response = response
        self.error = error
        self.kwargs = None

    def get(self, url, **kwargs):
        self.kwargs = {"url": url, **kwargs}
        if self.error:
            raise self.error
        return self.response

def test_fetch_aqi_validates_and_returns_metadata():
    session = FakeSession(FakeResponse({
        "status": "ok",
        "data": {
            "aqi": 42,
            "city": {"name": "Example Station"},
            "time": {"s": "2026-01-01 10:00:00"},
        },
    }))
    result = app.fetch_aqi("Example City", "test-token", session=session)
    assert result["aqi"] == 42
    assert result["level"] == "Good"
    assert result["station"] == "Example Station"
    assert session.kwargs["timeout"] == app.REQUEST_TIMEOUT_SECONDS
    assert session.kwargs["params"]["token"] == "test-token"

def test_fetch_aqi_rejects_empty_city():
    with pytest.raises(ValueError):
        app.fetch_aqi("  ", "test-token", session=FakeSession())

def test_fetch_aqi_rejects_missing_token():
    with pytest.raises(app.AQIProviderError):
        app.fetch_aqi("Delhi", "", session=FakeSession())

def test_fetch_aqi_handles_provider_status_failure():
    session = FakeSession(FakeResponse({"status": "error", "data": "unknown station"}))
    with pytest.raises(app.AQIProviderError):
        app.fetch_aqi("NotARealPlace", "test-token", session=session)

def test_fetch_aqi_rejects_invalid_aqi():
    for value in (-2, True, "42", None):
        session = FakeSession(FakeResponse({"status": "ok", "data": {"aqi": value}}))
        with pytest.raises(app.AQIProviderError):
            app.fetch_aqi("Delhi", "test-token", session=session)

def test_fetch_aqi_handles_invalid_json():
    session = FakeSession(FakeResponse(ValueError("bad json")))
    with pytest.raises(app.AQIProviderError):
        app.fetch_aqi("Delhi", "test-token", session=session)

def test_fetch_aqi_handles_timeout():
    session = FakeSession(error=requests.Timeout())
    with pytest.raises(app.AQIProviderError, match="too long"):
        app.fetch_aqi("Delhi", "test-token", session=session)

def test_fetch_aqi_handles_connection_error():
    session = FakeSession(error=requests.ConnectionError())
    with pytest.raises(app.AQIProviderError, match="connect"):
        app.fetch_aqi("Delhi", "test-token", session=session)
