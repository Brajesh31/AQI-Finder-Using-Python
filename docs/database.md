# 🗃️ Database and persistence

## Current status

The current AQI Finder application does not use a database. It performs an on-demand WAQI request and displays the returned result. It does not store searches, AQI observations, accounts, or location history.

## Why no database is appropriate today

A persistent store is not needed for one-time lookups. Adding a database creates responsibilities for schema migrations, backups, access controls, retention, privacy notices, deletion, and data correctness. Those costs are not justified unless a concrete feature requires persistence.

## Future persistence decision

A local history feature could potentially store a minimal record:

| Field | Purpose | Privacy consideration |
|---|---|---|
| `station_id` | Provider station identifier | Avoid more location detail than necessary |
| `station_name` | Human-readable source | May reveal geographic context |
| `aqi_value` | Numeric observation | Preserve the provider value |
| `observed_at` | Provider observation time | Never substitute retrieval time |
| `retrieved_at` | Time the app received the response | Record timezone consistently |
| `provider` | Data-source provenance | Preserve attribution |
| `index_method` | Category method | Prevent mixing incompatible index systems |

This is a proposal, not an implemented schema. Before adding persistence, decide whether data is local or remote, whether location is sensitive, how users delete history, how long data is retained, and how corrected or stale observations are represented.

## Data integrity

Never silently combine readings from different stations, time windows, or AQI methodologies. A future trend chart must show station identity, time coverage, missing observations, source, and index method. Missing data must not be plotted as zero.
