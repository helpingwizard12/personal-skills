---
tags: [skill-creator]
max_turns: 30
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

add a function save_avatar(user_id, filename, data) in app/avatars.py that saves an uploaded profile picture under uploads/avatars/ and returns the path it was saved to. filename and data (bytes) come straight from the multipart upload. add tests too

Input files: README.md, app/config.py
