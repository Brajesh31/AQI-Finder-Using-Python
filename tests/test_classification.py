import importlib.util
from pathlib import Path

import pytest

APP_PATH = Path(__file__).resolve().parents[1] / "AQI PYTHON"
spec = importlib.util.spec_from_file_location("aqi_app", APP_PATH)
app = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(app)

@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (0, "Good"), (50, "Good"),
        (51, "Moderate"), (100, "Moderate"),
        (101, "Unhealthy for Sensitive Groups"), (150, "Unhealthy for Sensitive Groups"),
        (151, "Unhealthy"), (200, "Unhealthy"),
        (201, "Very Unhealthy"), (300, "Very Unhealthy"),
        (301, "Hazardous"), (500, "Hazardous"),
    ],
)
def test_aqi_category_boundaries(value, expected):
    assert app.get_aqi_level(value) == expected

@pytest.mark.parametrize("value", [-1, True, "50", None, float("nan")])
def test_invalid_aqi_values_are_rejected(value):
    with pytest.raises(ValueError):
        app.get_aqi_level(value)
