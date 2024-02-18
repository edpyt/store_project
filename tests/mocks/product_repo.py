from src.application.product.exceptions import ProductIdNotExistError
from src.application.product.interfaces.persistence.repo import ProductRepo
from src.domain.product import entities
from src.domain.product.value_objects import ProductId, ProductProperty


class ProductRepoMock(ProductRepo):
    def __init__(self) -> None:
        self.products: dict[ProductId, entities.Product] = {}

    async def acquire_product_by_id(
        self, product_id: ProductId
    ) -> entities.Product:
        if product_id not in self.products:
            raise ProductIdNotExistError(product_id.to_raw())
        return self.products[product_id]

    async def add_product(self, product: entities.Product) -> None:
        self.products[product.id] = product

    async def get_existing_product_properties(self) -> set[ProductProperty]:
        product_properties = {
            product.product_property for product in self.products.values()
        }
        return product_properties
