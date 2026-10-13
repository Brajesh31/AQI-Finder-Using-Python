# Troubleshooting

## `ModuleNotFoundError: requests`

Activate the virtual environment and run `python -m pip install requests`.

## The window freezes

The network request is synchronous. Use a worker thread or asynchronous design with safe Tkinter callbacks.

## No AQI is returned

Check the city spelling, provider availability, network connection, token validity, and response status. Do not expose the token while diagnosing.
