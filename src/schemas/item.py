from pydantic import BaseModel, Field
from typing import Union

class Item(BaseModel):
    """
    Represents an item in the system.
    Moving this to a separate file allows us to reuse this model 
    across different parts of the app without circular imports.
    """
    name: str = Field(..., example="Laptop")
    description: Union[str, None] = Field(default=None, example="A powerful computing device.")
    price: float = Field(..., example=1200.50)
    tax: Union[float, None] = Field(default=None, example=120.05)

class ItemCreate(BaseModel):
    """
    Schema for creating a new item. 
    Notice we don't include 'item_id' here because 
    the server/database generates that!
    """
    name: str = Field(..., min_length=1, example="Smartphone")
    description: Union[str, None] = Field(default=None, example="A high-end mobile device.")
    price: float = Field(..., gt=0, example=699.99)
    tax: Union[float, None] = Field(default=None, example=55.99)