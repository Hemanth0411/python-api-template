from pydantic import BaseModel, Field
from typing import Union

class Item(BaseModel):
    """
    Represents an item in the system.
    """
    item_id: int = Field(..., json_schema_extra={"example": 1})
    name: str = Field(..., json_schema_extra={"example": "Laptop"})
    description: Union[str, None] = Field(default=None, json_schema_extra={"example": "A powerful computing device."})
    price: float = Field(..., json_schema_extra={"example": 1200.50})
    tax: Union[float, None] = Field(default=None, json_schema_extra={"example": 120.05})

class ItemCreate(BaseModel):
    """
    Schema for creating a new item. 
    """
    name: str = Field(..., min_length=1, json_schema_extra={"example": "Smartphone"})
    description: Union[str, None] = Field(default=None, json_schema_extra={"example": "A high-end mobile device."})
    price: float = Field(..., gt=0, json_schema_extra={"example": 699.99})
    tax: Union[float, None] = Field(default=None, json_schema_extra={"example": 55.99})