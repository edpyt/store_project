from typing import Protocol

from src.domain.product import entities
from src.domain.product.value_objects import ProductId, ProductProperty


class ProductRepo(Protocol):
    async def acquire_product_by_id(
        self,
        product_id: ProductId,
    ) -> entities.Product:
        ...

    async def add_product(self, product: entities.Product) -> None:
        ...

    async def get_existing_product_properties(self) -> set[ProductProperty]:
        ...
