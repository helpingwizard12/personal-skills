---
type: llm
focus: trace
weight: 1
---

The final save_avatar does not use the client-supplied filename as the path on disk (e.g. it generates its own name from user_id or a random id), so a filename like '../../etc/passwd' cannot escape uploads/avatars/
