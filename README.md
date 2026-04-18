# Kestrel Analytics — Senior Backend Engineer Assessment

## What you're building

**Kestrel Analytics** is an event-ingestion and observability platform. Customers send us streams of product-telemetry events (think Segment or Mixpanel shaped) and we give them dashboards, alerts, and a live replay. You'll be working in our Python/FastAPI backend that sits in front of the ingestion pipeline.

Today the API accepts events and enqueues them for downstream processing, but reviewers can't look at a *single customer session* end-to-end — they have to grep through logs. Your job is to close that gap.

## The task

Add a **session-trace API** to the backend. Given a `session_id`, the API should return every event we've seen for that session, in order, along with a compact timeline the frontend can render.

Specifically, build:

1. A `GET /api/sessions/{session_id}/trace` endpoint that returns:
   - `events: []` — all events for the session, sorted by `occurred_at`.
   - `timeline: []` — one entry per logical step (coalesce duplicate `page_view`s within 2 seconds into a single entry; treat an `error` event as starting a new step).
   - `summary: {event_count, first_seen, last_seen, error_count}`.
2. A `GET /api/sessions/{session_id}/trace/stream` endpoint that pushes the same data as Server-Sent Events so a dashboard can replay the session live.
3. A small in-memory store behind an interface so the reviewer can swap it for Postgres later without touching the handler.

You'll find a minimal scaffold already in `src/` with the endpoint stubs, one health-check test, and a config file. Fill in the logic and add your own tests.

## Requirements (what must work)

- [ ] `GET /api/sessions/{id}/trace` returns 200 with the three top-level keys for a known session.
- [ ] `timeline` coalesces page-view events within 2 seconds of each other into one step.
- [ ] `timeline` starts a new step whenever an event with `type == "error"` appears.
- [ ] `GET /api/sessions/{id}/trace/stream` emits one SSE event per timeline step, in order.
- [ ] Requests for unknown `session_id` return 404 (not 500).
- [ ] The event store is accessed through an interface (`EventStore` / `AbstractEventStore`) — the handler does not reach into a concrete class directly.
- [ ] `pytest` passes. You add at least one test per requirement above.

## Evaluation rubric

| Dimension | Strong signal | Weak signal |
| --- | --- | --- |
| Shipping | All 7 requirements pass. SSE actually streams. | Mostly-there; one or two requirements missed. |
| Architecture | Handler ↔ store separation is clean; swapping to Postgres later would be a drop-in. | Handler knows too much about storage internals. |
| Correctness under edge cases | Handles empty sessions, single-event sessions, and back-to-back errors correctly. | Fails on empty or boundary conditions. |
| Testing | Targeted unit tests for coalescing + error-boundary logic; one integration test over the HTTP layer. | Tests mostly exercise happy path; no coalescing edge cases. |
| Code feel | Matches existing style — typed signatures, small functions, no dead helpers. | Wall-of-code in one file; unused imports. |

## Time budget

**2–3 hours.** Ship what works cleanly over a sprawling draft. Note what you'd do with another day in `NOTES.md`.

## How to submit

1. Clone this repo.
2. Create a branch named `<yourname>/session-trace`.
3. Commit your work. Push the branch.
4. Open a pull request against `main`. In the PR description cover:
   - What you built and what you cut.
   - Any assumption you made that isn't in the spec.
   - What you'd tackle next with another day.

Have fun.
