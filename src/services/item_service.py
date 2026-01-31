from typing import Union
from schemas.item import Item

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
            "description": "Retrieved via ItemService"
        }