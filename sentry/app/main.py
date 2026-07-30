"""SENTRY FastAPI application entry point."""

from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    docs_url="/docs" if settings.debug else None,
)


@app.get("/health")
async def health():
    return {"status": "ok", "version": settings.app_version, "app": settings.app_name}
