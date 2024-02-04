from typing import Protocol

from src.application.product import dto


class ProductReader(Protocol):
    async def get_products(self) -> list[dto.ProductDTO]:
        raise NotImplementedError
