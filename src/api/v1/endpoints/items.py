from fastapi import APIRouter, Depends, status, Response
from typing import Union
from schemas.item import Item, ItemCreate
from services.item_service import ItemService

router = APIRouter()


def get_item_service():
    return ItemService()


@router.get("/{item_id}", response_model=Item)
def read_item(
    item_id: int,
    q: Union[str, None] = None,
    service: ItemService = Depends(get_item_service),
):
    """
    Retrieves an item by its ID.
    Notice we removed the '/items' prefix from the path.
    The main app will add that prefix globally later.
    """
    return service.get_item_by_id(item_id, q)


@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate, service: ItemService = Depends(get_item_service)):
    """Creates a new item and returns 201 Created."""
    return service.create_item(item)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, service: ItemService = Depends(get_item_service)):
    """Deletes an item and returns 204 No Content."""
    service.delete_item(item_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
