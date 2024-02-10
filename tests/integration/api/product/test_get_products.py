import json
from dataclasses import asdict

import pytest
from httpx import AsyncClient

from src.application.product.dto.products import ProductDTO


@pytest.mark.asyncio
async def test_get_all_products_without_created(client: AsyncClient) -> None:
    response = await client.get("/product/all")

    assert response.json() == []


@pytest.mark.asyncio
async def test_get_all_products_with_created(
    client: AsyncClient, created_product_dto: ProductDTO,
) -> None:
    created_product_serialized = json.loads(
        json.dumps(asdict(created_product_dto), default=str),
    )

    response = await client.get("/product/all")

    assert response.json() == [created_product_serialized]
