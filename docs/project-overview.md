# 🌍 Project overview

## 1. Purpose

AQI Finder Using Python is a small desktop application that lets a person enter a city or supported monitoring-station query and request an air-quality reading from the World Air Quality Index (WAQI) feed. The application presents the returned numeric AQI with a category label.

The goal is to make a remote reading easier to request and understand through a simple local desktop interface. It is not an atmospheric sensor, an official health authority, or a forecasting model.

## 2. Current implementation

The repository's principal application file is `AQI PYTHON`. It contains:

- a Tkinter window and input controls;
- a Requests-based WAQI feed call;
- response validation and user-facing failure states;
- a category function mapping numeric values to six labels;
- optional station name and observation time display when the provider supplies them.

The application performs an on-demand lookup. No scheduled refresh, local history, database, cloud backend, account system, or automated geolocation is implemented.

## 3. User journey

1. Install Python, Tkinter, and Requests.
2. Configure a personal WAQI token using `WAQI_TOKEN`.
3. Launch the desktop program.
4. Enter a city or supported station query.
5. Request the reading.
6. Review the AQI number, project category, and available provider metadata.
7. Consult local official guidance for decisions that may affect health or outdoor activity.

## 4. What an AQI reading means

AQI is an index calculated from pollutant measurements using a particular methodology. Its numerical scale, pollutants, averaging periods, breakpoint tables, and category terminology may vary by country or provider. The application's category function preserves the breakpoints from the original prototype. It must not be presented as a universal standard.

The API may identify a specific monitoring station. A station reading does not necessarily represent every neighbourhood in a city. Local topography, weather, traffic, industrial sources, and station coverage can create meaningful differences across locations.

## 5. Non-goals and boundaries

The current application does not:

- measure pollutants directly;
- guarantee complete station coverage;
- predict future AQI;
- provide medical diagnosis or personalized medical advice;
- prove that a city-wide average is represented by one station;
- store user searches or precise location history;
- provide a public multi-user website or server API.

## 6. Intended quality attributes

- **Clarity:** show what value was retrieved and whether it was a station observation.
- **Resilience:** handle timeout, network, HTTP, provider-status, and malformed-response conditions.
- **Responsiveness:** keep the Tkinter event loop usable while a request is in progress.
- **Security:** keep provider credentials out of source control and avoid exposing tokens in errors.
- **Testability:** isolate category mapping and provider response handling from widgets.
- **Honesty:** show missing metadata as missing and avoid overstating the health meaning of a reading.

## 7. Success criteria for future releases

A release should be considered ready only when setup works in a clean environment, the classification boundaries have automated tests, provider failures have deterministic mocked tests, credentials are not present in source, and the GUI has been reviewed on the target operating systems. Claims about index standards or medical guidance require separate authoritative review.
