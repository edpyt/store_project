from sqlalchemy import select

from src.application.product import dto
from src.application.product.interfaces import ProductReader
from src.infrastructure.db.models.product import Product
from src.infrastructure.db.repositories.base import SQLAlchemyRepo


class ProductReaderImpl(SQLAlchemyRepo, ProductReader):
    async def get_products(self) -> list[dto.ProductDTO]:
        stmt = select(Product)
        result = await self._session.scalars(stmt)
        return list(
            map(
                lambda product: dto.ProductDTO(
                    title=product.title,
                    price=product.price,
                    weight=product.weight,
                ),
                result.all(),
            )
        )
