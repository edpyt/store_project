from typing import Protocol

from src.domain.product import entities
from src.domain.product.value_objects import ProductId


class ProductRepo(Protocol):
    async def acquire_product_by_id(
        self, product_id: ProductId,
    ) -> entities.Product:
        ...
