from fastapi import APIRouter, Depends
from typing import Union
from schemas.item import Item
from services.item_service import ItemService

router = APIRouter()

def get_item_service():
    return ItemService()

@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int, q: Union[str, None] = None, service: ItemService = Depends(get_item_service)
):
    """
    Retrieves an item by its ID. 
    Notice we removed the '/items' prefix from the path. 
    The main app will add that prefix globally later.
    """
    return service.get_item_by_id(item_id, q)
