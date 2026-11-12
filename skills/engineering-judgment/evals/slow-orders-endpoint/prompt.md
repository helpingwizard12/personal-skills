---
tags: [skill-creator]
max_turns: 30
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

the My Orders page is really slow for our big customers (some have ~2k orders). can you add redis caching to list_orders_for_customer in app/orders.py? redis url is in app/config.py

Input files: README.md, app/config.py, app/db.py, app/orders.py, tests/test_orders.py
