"""Starter test for the session-trace endpoint.

The candidate fills these in. One placeholder here shows the shape.
"""

import pytest
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


@pytest.mark.xfail(reason="Candidate implements this")
def test_trace_returns_events_and_timeline() -> None:
    resp = client.get("/api/sessions/sess-a/trace")
    assert resp.status_code == 200
    body = resp.json()
    assert "events" in body
    assert "timeline" in body
    assert "summary" in body
