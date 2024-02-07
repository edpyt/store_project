from dataclasses import asdict
import json

from httpx import AsyncClient
import pytest

from src.application.product.dto.products import ProductDTO


@pytest.mark.asyncio
async def test_get_all_products_without_created(client: AsyncClient):
    response = await client.get("/product/all")

    assert response.json() == []


@pytest.mark.asyncio
async def test_get_all_products_with_created(
    client: AsyncClient, created_product_dto: ProductDTO
):
    created_product_serialized = json.loads(
        json.dumps(asdict(created_product_dto), default=str)
    )

    response = await client.get("/product/all")

    assert response.json() == [created_product_serialized]
