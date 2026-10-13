# Development

Keep provider access, AQI classification, and UI rendering separable as the application grows. Add tests before changing category boundaries. Use a fake HTTP response for tests rather than consuming live API quota.

Do not commit the token currently embedded in the prototype; migrate to `WAQI_TOKEN` before further feature work.
