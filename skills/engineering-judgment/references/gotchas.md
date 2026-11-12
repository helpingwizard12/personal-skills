# Gotchas

Failure modes experienced engineers check for by reflex. Scan a design, diff, or plan against the categories that apply; most changes touch two or three. Each entry gives the question to ask and what a good answer looks like. These are original working guidance, not quotations from the source books.

## Retries and idempotency

Ask: If this runs twice — a client retry, a queue redelivery, a timeout after the side effect succeeded — what happens?

Charging a card, sending an email, creating a record, or calling a partner API on retry can duplicate the effect. Use an idempotency key the downstream system honours, a unique constraint, or a "check then act" guarded by a transaction. Retry only errors that are safe to retry, with backoff and a cap.

## Concurrency and ordering

Ask: What if two of these happen at the same time, or arrive out of order?

Read-modify-write without a lock or conditional update loses writes. Counters, balances, inventory, and "only one active X" rules need atomic updates or constraints. Background jobs and webhooks can arrive out of order or after the thing they refer to was deleted.

## Time and time zones

Ask: Which time zone is this in, and what happens at midnight, month end, and DST changes?

Store and compare instants in UTC; convert to a user's zone only for display or for user-facing buckets ("their Monday"). Naive datetimes mixed with aware ones cause off-by-hours bugs that show up only for some users. Tests should cover a non-UTC zone and a boundary.

## Migrations and locks

Ask: How long does this lock the table, and can the old and new code both run against it?

On large tables, adding indexes without `CONCURRENTLY` (Postgres), rewriting columns, or adding constraints that validate every row can block writes. Backfill in batches. Use expand/contract so each deploy is compatible with the previous one. A code rollback does not undo a data change — keep the old data until the new path is proven, or take a backup.

## Compatibility

Ask: Who else reads or writes this — old app versions, other services, exports, analytics jobs?

Removing or renaming a field, changing an error shape, tightening validation, or changing ordering can break consumers the interface never documented. Keep the old behaviour until usage evidence says it is gone.

## Personal and secret data

Ask: Does this write personal data, tokens, or secrets anywhere new — logs, error messages, analytics, caches, third parties?

Logging a full request body or user object often leaks emails, addresses, or tokens. Log identifiers, not contents. Check retention and who can read the destination.

## Failure handling

Ask: When the dependency is slow or down, what does the user see, and does anything get lost?

Set timeouts on every network call. Decide between failing fast, degrading, and queueing for later. Writes that must not be lost (orders, signups, emails) need a durable record before the side effect — for example, a row in the same transaction that a worker processes (the outbox pattern) — rather than a fire-and-forget call.

## Hidden and growing costs

Ask: What does this cost at ten times today's volume, and who pays it?

Per-request API or model calls, unbounded queries, N+1 queries, fan-out jobs, high-cardinality metrics, and log volume grow quietly. Look for the loop that makes a call per item.

## Caching

Ask: What is slow, and why — and how will the cache be invalidated?

A cache over a slow query hides the cause and adds staleness and invalidation bugs. Fix the query (index, join instead of N+1, pagination) first; cache only when the work is inherently expensive and staleness is acceptable.

## Over-engineering

Ask: Which concrete, near-term change does this abstraction make easier?

Strategy patterns, plugin systems, factories, and configuration for a single implementation add reading cost without paying anything back. Prefer the direct version until a second real case appears.
