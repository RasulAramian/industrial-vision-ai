"""FastAPI application entry point."""

from fastapi import FastAPI

app = FastAPI(
    title="Industrial Vision AI",
    description="API for industrial image anomaly detection.",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    """Return the service health status."""
    return {"status": "ok"}


@app.get("/")
def root() -> dict[str, str]:
    """Return basic service information."""
    return {
        "name": "Industrial Vision AI",
        "status": "initializing",
    }
