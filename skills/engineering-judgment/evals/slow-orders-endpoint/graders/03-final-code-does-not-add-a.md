---
type: llm
focus: trace
weight: 1
---

The final code does not add a Redis cache without first removing the N+1 queries; if any cache is added, the response explains how it is invalidated when orders change
