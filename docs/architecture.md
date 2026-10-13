# Architecture

The application is a single Tkinter process. `find_aqi` reads the city entry, calls the WAQI feed, and updates a result label. `get_aqi_level` maps the numeric AQI to a display category.

The UI and network call currently run on the same thread, so slow requests can freeze the window. A production-quality revision should separate I/O from the UI thread.
