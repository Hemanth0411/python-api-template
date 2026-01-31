async def test_read_item(client):
    """Checks if we can retrieve an item correctly."""
    response = await client.get("/api/v1/items/1")
    
    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == 1
    assert "name" in data

async def test_create_item(client):
    """Checks if we can create an item."""
    new_item = {
        "name": "Test Item",
        "price": 10.5,
        "description": "Integration Test"
    }
    response = await client.post("/api/v1/items/", json=new_item)
    
    assert response.status_code == 201
    assert response.json()["name"] == "Test Item"

async def test_delete_item_not_found(client):
    """Checks if the 404 logic we wrote actually works."""
    response = await client.delete("/api/v1/items/404")
    assert response.status_code == 404