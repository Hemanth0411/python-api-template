from fastapi import FastAPI
from api.v1.api import api_router
from core.config import settings
from core.logging_config import setup_logging
from api.middleware import log_requests

setup_logging()

# Define tags for Swagger UI Documentation
tags_metadata = [
    {
        "name": "Default",
        "description": "General-purpose and health check endpoints.",
    },
    {
        "name": "Items",
        "description": "Manage items in the system.",
    },
]

app = FastAPI(
    title=settings.APP_TITLE,
    description="Refactored for scalability using Layered Architecture.",
    version=settings.APP_VERSION,
    openapi_tags=tags_metadata
)

app.middleware("http")(log_requests)

app.include_router(api_router, prefix="/api/v1")

@app.get("/", tags=["Default"])
def read_root():
    """Health check endpoint."""
    return {"status": "ok", "message": "Welcome to the Modular Python API!"}