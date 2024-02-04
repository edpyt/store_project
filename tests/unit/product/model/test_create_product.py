import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.db.models.product import Product


@pytest.mark.asyncio
async def test_create_product(session: AsyncSession):
    product = Product(title='milk', cost=2)

    assert product.title == 'milk'
    assert product.cost == 2
