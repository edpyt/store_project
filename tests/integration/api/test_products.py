from httpx import AsyncClient
import pytest


@pytest.mark.asyncio
async def test_get_all_products(client: AsyncClient):
    response = await client.get('/product/all')
    await response.json() == []


@pytest.mark.asyncio
async def test_get_unexpired_products(client: AsyncClient):
    response = await client.get('/product/unexpired')
    await response.json() == []


@pytest.mark.asyncio
async def test_get_single_product(client: AsyncClient, product: Product):
    response = await client.get(f'/product/{product.uuid}')
    await response.json() == product.to_json()


@pytest.mark.asyncio
async def test_delete_product(admin_client: AsyncClient, product: Product):
    await admin_client.delete(f'/product/{product.uuid}')
    await Product.all().count() == 0


@pytest.mark.asyncio
async def test_update_product(admin_client: AsyncClient, product: Product):
    response = await admin_client.patch(f'/product/{product.uuid}')
    await response.json() == {'status': 'updated'}
