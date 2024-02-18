import json
from dataclasses import asdict

from httpx import AsyncClient

from src.application.product.dto.products import ProductDTO


async def test_get_all_products_without_created(client: AsyncClient) -> None:
    response = await client.get("/product/all")

    assert response.json() == []


async def test_get_all_products_with_created(
    created_product_dto: ProductDTO, client: AsyncClient,
) -> None:
    created_product_serialized = json.loads(
        json.dumps(asdict(created_product_dto), default=str),
    )

    response = await client.get("/product/all")

    assert response.json() == [created_product_serialized]
