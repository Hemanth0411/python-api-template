from fastapi import FastAPI
from api.endpoints import items  
from core.config import settings

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

app.include_router(items.router, prefix="/items", tags=["Items"])

@app.get("/", tags=["Default"])
def read_root():
    """Health check endpoint."""
    return {"status": "ok", "message": "Welcome to the Modular Python API!"}