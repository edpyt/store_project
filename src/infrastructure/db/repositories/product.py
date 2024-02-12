from sqlalchemy import select

from src.application.product.dto import ProductDTO  # type: ignore[attr-defined]
from src.application.product.interfaces import ProductReader
from src.infrastructure.db.models.product import Product
from src.infrastructure.db.repositories.base import SQLAlchemyRepo


class ProductReaderImpl(SQLAlchemyRepo, ProductReader):
    async def get_products(self) -> list[ProductDTO]:
        stmt = select(Product)
        result = await self._session.scalars(stmt)
        return [
            ProductDTO(
                title=product.title,
                price=product.price,
                weight=product.weight,
            )
            for product in result.all()
        ]
