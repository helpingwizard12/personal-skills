---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write]
---

I need to split the `full_name` column in our `users` table (Postgres, ~40M rows) into `first_name` and `last_name`. We can't take downtime, and some old versions of our mobile app still read `full_name` from the API and will be around for months. How should I do this?
