import pytest
from src.application.product import dto

from src.application.product.interfaces import ProductReader
from src.infrastructure.db.models.product import Product


@pytest.mark.asyncio
async def test_get_all_products(products_reader: ProductReader):
    assert await products_reader.get_products() == []


@pytest.mark.asyncio
async def test_get_products_with_created(
    products_reader: ProductReader, created_product: Product
):
    product_dto = dto.ProductDTO(
        title=created_product.title,
        price=created_product.price,
        weight=created_product.weight,
    )

    assert await products_reader.get_products() == [product_dto]
