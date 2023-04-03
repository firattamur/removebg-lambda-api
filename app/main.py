"""Main module for the app."""

from fastapi import FastAPI
from mangum import Mangum

from app.api.v1.routers import router as v1_router
from app.core.config import STAGE
from app.core.logging import LoggerRouterHandler, logger

app = FastAPI(
    title="RemoveBG API",
    description="FastAPI backend for Image Background Remover",
    version="1.0.0",
    root_path=f"/{STAGE}",
)

app.router.route_class = LoggerRouterHandler
app.router.include_router(v1_router, prefix="/api/v1", tags=["removebg"])


@app.get("/status")
def health():
    """Health check endpoint."""
    return {"status": "ok"}


handler = Mangum(app=app)
handler = logger.inject_lambda_context(handler, clear_state=True)
