---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write]
---

We're a 5-person eng team running a Django monolith on Postgres, about 2k daily active users. Our new CTO wants to split it into microservices "so we can scale". Deploys take 25 minutes and the test suite is flaky, which is the thing that actually annoys everyone. Should we do the microservices split? Give me your recommendation.
