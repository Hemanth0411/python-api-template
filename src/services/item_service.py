from typing import Union

from fastapi import HTTPException
from schemas.item import Item, ItemCreate


class ItemService:
    """
    This class handles the logic for Items.
    It doesn't care about 'requests' or 'responses';
    it only cares about 'Business Data'.
    """

    def get_item_by_id(self, item_id: int, q: Union[str, None] = None) -> dict:
        return {
            "name": f"Item {item_id}",
            "price": 99.99,
            "item_id": item_id,
            "q": q,
            "description": "Retrieved via ItemService",
        }

    def create_item(self, item_data: ItemCreate) -> Item:
        # Business logic: In a real app, save to DB here.
        # For now, we simulate by adding an ID
        return Item(item_id=999, **item_data.model_dump())

    def delete_item(self, item_id: int):
        # Business logic: Check if exists, then delete.
        if item_id == 404:
            raise HTTPException(status_code=404, detail="Item not found")
        return True
