# Kestrel session-trace assessment

This is your Palannon coding assessment. Your candidate-facing instructions are in [`ASSESSMENT.md`](./ASSESSMENT.md) — **read that first**.

## Quick start

```bash
pip install -r requirements.txt
pytest        # one smoke test should pass out of the box
uvicorn src.main:app --reload --port 8080
```

Then hit `http://127.0.0.1:8080/health` — you should get `{"status": "ok"}`.

The stubs you need to fill in live under `src/session_trace/`.

## What to do next

Open [`ASSESSMENT.md`](./ASSESSMENT.md). It has the problem statement, requirements, rubric, time budget, and submission instructions.
