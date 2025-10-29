# Import necessary modules from FastAPI and Pydantic
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Union

# --- Pydantic Models ---
# Pydantic models define the structure, data types, and validation for your API data.
# They are used for both request bodies and response models.

class Item(BaseModel):
    """Represents an item in the system."""
    name: str = Field(..., example="Laptop")
    description: Union[str, None] = Field(default=None, example="A powerful computing device.")
    price: float = Field(..., example=1200.50)
    tax: Union[float, None] = Field(default=None, example=120.05)


# --- Application Metadata ---
# This information is used in the auto-generated OpenAPI documentation.
tags_metadata = [
    {
        "name": "Default",
        "description": "General-purpose and health check endpoints.",
    },
    {
        "name": "Items",
        "description": "Manage items in the system. Allows you to create and retrieve items.",
    },
]

# --- FastAPI App Instance ---
# This is the main application object.
app = FastAPI(
    title="Python API Template",
    description="A professional, modern template for building robust Python REST APIs.",
    version="0.1.0",
    openapi_tags=tags_metadata
)

# --- API Endpoints ---

@app.get("/", tags=["Default"])
def read_root():
    """
    A simple health check endpoint.
    
    Returns a status message indicating the API is running.
    """
    return {"status": "ok", "message": "Welcome to the Python API Template!"}


@app.get("/items/{item_id}", response_model=Item, tags=["Items"])
def read_item(item_id: int, q: Union[str, None] = None):
    """
    Retrieves an item by its ID.
    
    This endpoint demonstrates path parameters, query parameters, and a response model.
    """
    # In a real application, you would fetch this data from a database.
    return {"name": "Example Item", "price": 50.0, "item_id": item_id, "q": q}