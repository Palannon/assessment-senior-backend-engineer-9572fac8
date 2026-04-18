"""HTTP endpoints for the session-trace assessment.

TODO for the candidate:
- Implement GET /api/sessions/{session_id}/trace.
- Implement GET /api/sessions/{session_id}/trace/stream (SSE).
- Return 404 when the session is unknown.
"""

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from .store import EventStore, InMemoryEventStore

router = APIRouter()

# The handler must go through this interface — not InMemoryEventStore directly.
# In a real app we'd inject this, but for the assessment a module-level store
# keeps the reviewer surface small. Feel free to refactor.
store: EventStore = InMemoryEventStore.with_seed_data()


@router.get("/sessions/{session_id}/trace")
def get_session_trace(session_id: str):
    # TODO: fetch events from the store, sort by occurred_at, compute the
    # timeline (see ASSESSMENT.md for the coalescing rules), and return the
    # three top-level keys: events, timeline, summary.
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/sessions/{session_id}/trace/stream")
def stream_session_trace(session_id: str):
    # TODO: emit one SSE event per timeline step, in order.
    def _gen():
        yield "event: stub\ndata: implement me\n\n"

    return StreamingResponse(_gen(), media_type="text/event-stream")
