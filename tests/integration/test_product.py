from litestar.testing.client import AsyncTestClient

from src.infrastructure.db.models import Product


async def test_get_products(test_client: AsyncTestClient) -> None:
    response = await test_client.get("/product/all")

    assert response.status_code == 200
    assert response.json() == []


async def test_create_product(test_client: AsyncTestClient) -> None:
    response = await test_client.post("/product/create/", json={})

    assert response.status_code == 201


async def test_update_product(
    test_client: AsyncTestClient, created_product: Product
) -> None:
    response = await test_client.patch(
        f"/product/update/{created_product.id}/", json={}
    )

    assert response.status_code == 200


async def test_delete_product(
    test_client: AsyncTestClient, created_product: Product
) -> None:
    response = await test_client.delete(f"/product/delete/{created_product.id}/")

    assert response.status_code == 200
