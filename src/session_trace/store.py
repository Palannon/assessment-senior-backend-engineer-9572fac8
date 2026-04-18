"""Storage interface for session events.

Candidate: implement the InMemoryEventStore methods below. Keep the public
surface on `EventStore` stable — the reviewer may swap in a Postgres-backed
implementation behind the same interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass(frozen=True)
class Event:
    session_id: str
    type: str               # e.g. "page_view", "click", "error"
    occurred_at: datetime
    payload: dict = field(default_factory=dict)


class EventStore(ABC):
    """The handler only uses this interface."""

    @abstractmethod
    def get_events(self, session_id: str) -> list[Event]:
        """Return every event for the given session_id, sorted by occurred_at.

        Return an empty list if the session is unknown; the router translates
        that into a 404.
        """


class InMemoryEventStore(EventStore):
    """Simple in-process store seeded with a couple of demo sessions."""

    def __init__(self, events: list[Event] | None = None) -> None:
        self._events: list[Event] = events or []

    @classmethod
    def with_seed_data(cls) -> "InMemoryEventStore":
        now = datetime(2026, 4, 1, 12, 0, tzinfo=timezone.utc)
        demo = [
            Event("sess-a", "page_view", now, {"path": "/"}),
            Event("sess-a", "page_view", now.replace(second=1), {"path": "/pricing"}),
            Event("sess-a", "click", now.replace(second=5), {"target": "buy"}),
            Event("sess-a", "error", now.replace(second=7), {"code": "payment_declined"}),
            Event("sess-a", "page_view", now.replace(second=30), {"path": "/help"}),
        ]
        return cls(demo)

    # TODO(candidate): implement this.
    def get_events(self, session_id: str) -> list[Event]:
        raise NotImplementedError("Implement InMemoryEventStore.get_events")
