import pytest

from src.application.product.interfaces import ProductReader


@pytest.mark.asyncio
async def test_get_all_products(products_reader: ProductReader):
    assert await products_reader.get_products() == []
