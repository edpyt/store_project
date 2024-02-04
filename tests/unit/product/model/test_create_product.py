import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.db.models.product import Product


@pytest.mark.asyncio
async def test_create_product(session: AsyncSession):
    product = Product(title='milk', cost=2, weight=1)

    session.add(product)
    await session.commit()
    await session.refresh(product)

    assert product.title == 'milk'
    assert product.cost == 2
