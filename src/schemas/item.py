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