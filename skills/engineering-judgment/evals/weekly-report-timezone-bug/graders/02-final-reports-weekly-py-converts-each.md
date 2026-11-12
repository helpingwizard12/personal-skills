---
type: llm
focus: trace
weight: 1
---

The final reports/weekly.py converts each timestamp into the user's IANA time zone (e.g. zoneinfo.ZoneInfo(user_timezone)) before computing the week
