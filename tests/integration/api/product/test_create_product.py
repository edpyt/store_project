import pytest
from httpx import AsyncClient


@pytest.mark.skip
async def test_create_product(client: AsyncClient) -> None:
    response = await client.post(
        "/product/create/",
        data={"title": "test", "price": "0.1", "weight": 0.5},
    )

    assert response.status_code == 201
    assert response.json() == {"message": "Created product!"}


@pytest.mark.parametrize("create_product_data", [
    {"tsti": "dsaj", "dsajdjsa": .1, "erd": "E"},
    {"dsad": .1},
    [1, 2, 3, 4],
])
async def test_wrong_create_product(
    client: AsyncClient, create_product_data: dict[str, str | float] | list[int],
) -> None:
    response = await client.post("/product/create/", data=create_product_data)

    assert response.status_code == 400
