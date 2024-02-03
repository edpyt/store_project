from sqlalchemy import select

from src.application.product import dto
from src.application.product.interfaces import ProductReader
from src.infrastructure.db.models.product import Product
from src.infrastructure.db.repositories.base import SQLAlchemyRepo


class ProductReaderImpl(SQLAlchemyRepo, ProductReader):
    async def get_products(self) -> list[dto.Product]:
        stmt = select(Product)
        result = await self._session.scalar(stmt)
        return list(map(dto.Product, result))
