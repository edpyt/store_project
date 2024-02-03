import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.product.interfaces import ProductReader
from src.infrastructure.db.repositories import ProductReaderImpl


@pytest.fixture
def products_reader(session: AsyncSession) -> ProductReader:
    return ProductReaderImpl(session)
