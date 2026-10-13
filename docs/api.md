# External API

The application calls the WAQI feed endpoint:

`https://api.waqi.info/feed/{city}/?token={token}`

The current code expects a JSON object with `status`, and when successful, `data.aqi`. Provider availability, quota, attribution, and terms may change. Validate the complete response and keep the token private.
