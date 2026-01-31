import pytest
from httpx import ASGITransport, AsyncClient

from src.main import app


@pytest.fixture
async def client():
    """
    Creates a specialized test client for our FastAPI app.
    Using 'ASGITransport' allows us to test the app without
    actually starting a real network server.
    """
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac
