from typing import Annotated

from litestar import Controller, get, post
from litestar.params import Dependency

from src.application.product import dto
from src.application.product.interfaces.persistence.reader import ProductReader


class ProductController(Controller):
    path = "/product"

    @get("/all")
    async def get_all_products(
        self,
        product_reader: Annotated[ProductReader, Dependency(skip_validation=True)],
    ) -> list[dto.ProductDTO]:
        """Get all products endpoint.

        :param product_reader: ProductReader depends object
        """
        return await product_reader.get_products()


    @post("/create/")
    async def create_product(  # type: ignore
        self,
        product: dto.ProductDTO,
        product_reader: Annotated[ProductReader, Dependency(skip_validation=True)],
    ) -> dict[str, str]:
        """Create product endpoint.

        :param product: Product DTO object
        :param product_reader: ProductReader depends object
        """
        ...
