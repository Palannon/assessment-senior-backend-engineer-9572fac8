"""FastAPI entrypoint for the session-trace assessment."""

from fastapi import FastAPI

from .session_trace.router import router as session_trace_router

app = FastAPI(
    title="Kestrel session-trace",
    version="0.1.0",
    description="Candidate assessment app.",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(session_trace_router, prefix="/api", tags=["session-trace"])
