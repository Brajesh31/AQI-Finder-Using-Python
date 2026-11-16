# 📊 AQI methodology and interpretation

## 1. What the application currently does

The application receives a numeric `aqi` value from the WAQI response and maps that value to a display label. It does not calculate AQI from raw PM2.5, PM10, ozone, nitrogen dioxide, sulphur dioxide, or carbon monoxide measurements itself. The provider supplies the displayed AQI value.

## 2. Project category mapping

The following ranges are preserved from the original project classification function:

| Numeric value | Project label |
|---:|---|
| 0–50 | Good |
| 51–100 | Moderate |
| 101–150 | Unhealthy for Sensitive Groups |
| 151–200 | Unhealthy |
| 201–300 | Very Unhealthy |
| Above 300 | Hazardous |

The code accepts non-negative numeric values. Invalid values, booleans, missing values, or negative numbers should be rejected rather than assigned a category.

## 3. Important standard limitation

AQI is not one globally identical calculation. Authorities may differ in pollutant selection, averaging windows, concentration breakpoints, interpolation methods, rounding rules, and health statements. Therefore, the table above should be described as the mapping configured in this project, not as a universally authoritative AQI scale.

Before adding a jurisdiction selector or health recommendations, decide which official index is intended, identify a current authoritative reference, implement its complete pollutant and breakpoint rules, and add boundary tests. Do not simply rename categories while retaining incompatible breakpoints.

## 4. Station and time context

The provider may return a station name and an observation timestamp. Displaying this context helps users interpret the result. It does not guarantee that the sensor is nearby, currently calibrated, or representative of the entire city. A missing timestamp must not be replaced with the computer's current time and portrayed as the observation time.

## 5. Communicating uncertainty

A useful reading should communicate:

- numeric AQI value;
- category label and the index mapping used;
- station name, when returned;
- provider observation time, when returned;
- source attribution;
- an explanation when the reading is unavailable.

Avoid presenting false precision. Do not turn one station reading into a city-wide guarantee. Do not imply that a category predicts an individual's medical outcome.

## 6. Health-safety boundary

This tool is informational and is not medical advice. People with health concerns should follow local public-health guidance and advice from qualified healthcare professionals. Do not use this project as an emergency warning system. A missing or stale API response does not mean the air is safe.

## 7. Validation examples for tests

| Input | Expected label or result |
|---:|---|
| 0 | Good |
| 50 | Good |
| 51 | Moderate |
| 100 | Moderate |
| 101 | Unhealthy for Sensitive Groups |
| 150 | Unhealthy for Sensitive Groups |
| 151 | Unhealthy |
| 200 | Unhealthy |
| 201 | Very Unhealthy |
| 300 | Very Unhealthy |
| 301 | Hazardous |
| -1 | Raise validation error |
| `True` | Raise validation error |
