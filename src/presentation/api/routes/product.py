from typing import Annotated

from litestar import Controller, get, post
from litestar.params import Dependency

from src.application.product.dto.products import ProductDTO
from src.application.product.interfaces.persistence.reader import ProductReader


class ProductController(Controller):  # type: ignore[misc]
    path = "/product"

    @get("/all")  # type: ignore[misc]
    async def get_all_products(
        self,
        product_reader: Annotated[ProductReader, Dependency(skip_validation=True)],
    ) -> list[ProductDTO]:
        """Get all products endpoint.

        :param product_reader: ProductReader depends object
        """
        return await product_reader.get_products()

    @post("/create/")  # type: ignore[misc]
    async def create_product(  # type: ignore[empty-body]
        self,
        product: ProductDTO,
        product_reader: Annotated[ProductReader, Dependency(skip_validation=True)],
    ) -> dict[str, str]:
        """Create product endpoint.

        :param product: Product DTO object
        :param product_reader: ProductReader depends object
        """
        ...
