from typing import Protocol

from src.application.product.dto import ProductDTO  # type: ignore[attr-defined]


class ProductReader(Protocol):
    async def get_products(self) -> list[ProductDTO]:
        raise NotImplementedError
