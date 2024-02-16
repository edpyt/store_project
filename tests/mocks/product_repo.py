from src.application.product.exceptions import ProductIdNotExistError
from src.application.product.interfaces.persistence.repo import ProductRepo
from src.domain.product import entities
from src.domain.product.value_objects import ProductId


class ProductRepoMock(ProductRepo):
    def __init__(self) -> None:
        self.products: dict[ProductId, entities.Product] = {}

    async def acquire_product_by_id(self, product_id: ProductId) -> entities.Product:
        if product_id not in self.products:
            raise ProductIdNotExistError(product_id.to_raw())
        return self.products[product_id]
