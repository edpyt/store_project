from typing import Protocol
from uuid import UUID

from src.application.product.dto import ProductDTO  # type: ignore[attr-defined]


class ProductReader(Protocol):
    async def get_products(self) -> list[ProductDTO]:
        raise NotImplementedError

    async def get_product_by_id(self, id_: UUID) -> ProductDTO:
        raise NotImplementedError
