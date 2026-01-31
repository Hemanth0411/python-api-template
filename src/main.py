from fastapi import FastAPI
from api.endpoints import items  # Import the items router module

# --- Application Metadata ---
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
    title="Python API Template",
    description="Refactored for scalability using Layered Architecture.",
    version="0.2.0",
    openapi_tags=tags_metadata
)

# --- Router Registration ---
# This 'glues' the items routes to our main application.
# The prefix="/items" means all routes in items.py now start with /items/
app.include_router(items.router, prefix="/items", tags=["Items"])

@app.get("/", tags=["Default"])
def read_root():
    """Health check endpoint."""
    return {"status": "ok", "message": "Welcome to the Modular Python API!"}