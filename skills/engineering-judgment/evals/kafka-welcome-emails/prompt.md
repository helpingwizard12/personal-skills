---
tags: [skill-creator]
max_turns: 30
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

we're adding Kafka so that when a user signs up we publish a user_signed_up event and a consumer sends the welcome email. we get ~50 signups a day. stack is Django + Postgres, and we already run Celery + Redis for other background jobs. can you outline the Kafka setup (topics, partitions, consumer group, retention)?
