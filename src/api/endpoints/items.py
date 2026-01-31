from fastapi import APIRouter
from typing import Union
from schemas.item import Item

router = APIRouter()

@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int, q: Union[str, None] = None):
    """
    Retrieves an item by its ID. 
    Notice we removed the '/items' prefix from the path. 
    The main app will add that prefix globally later.
    """
    return {"name": "Example Item", "price": 50.0, "item_id": item_id, "q": q}