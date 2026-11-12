---
type: llm
focus: trace
weight: 1
---

The response identifies the root cause: timestamps are bucketed in UTC (utcfromtimestamp) instead of the user's own time zone, so the user_timezone argument is ignored
