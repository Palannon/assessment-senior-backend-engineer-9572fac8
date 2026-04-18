"""Smoke test — should pass out of the box.

Run with `pytest -q`. If this fails, something is wrong with your setup
before you start working on the assessment.
"""

from fastapi.testclient import TestClient

from src.main import app


def test_health_endpoint() -> None:
    client = TestClient(app)
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}
