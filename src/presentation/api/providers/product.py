from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from src.application.product.interfaces.persistence.reader import ProductReader
from src.infrastructure.db.repositories.product import ProductReaderImpl


async def create_product_reader_impl(
    session: AsyncSession,
) -> AsyncGenerator[ProductReader, None]:
    yield ProductReaderImpl(session)
