from httpx import AsyncClient
import pytest


@pytest.mark.asyncio
async def test_get_all_products(client: AsyncClient):
    response = await client.get('/product/all')
