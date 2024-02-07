import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_product(client: AsyncClient):
    response = await client.post(
        "/product/create/",
        data={"title": "test", "price": "0.1", "weight": 0.5},
    )

    assert response.status_code == 201
    assert response.json() == {"message": "Created product!"}
