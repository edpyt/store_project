from typing import Annotated

from dishka.integrations.litestar import Depends
from litestar import Controller, get, post

from src.application.product.commands.create_product import (
    CreateProductHandler,
)
from src.application.product.dto.products import ProductDTO
from src.application.product.interfaces.persistence.reader import ProductReader
from src.presentation.api.dto.product import CreateProductDTO, ReturnProductDTO


class ProductController(Controller):  # type: ignore[misc]
    path = "/product"
    tags = ["Product"]

    @get(
        "/all",
        summary="GET products",
        description="Get all products from database.",
    )  # type: ignore[misc]
    async def get_all_products(
        self,
        product_reader: Annotated[ProductReader, Depends()],
    ) -> list[ProductDTO]:
        """Get all products endpoint.

        :param product_reader: ProductReader depends object
        """
        return await product_reader.get_products()

    @post(
        "/create/",
        summary="CREATE product",
        description="Create product in database.",
        status_code=201,
        return_dto=ReturnProductDTO,
    )  # type: ignore[misc]
    async def create_product(  # type: ignore[empty-body]
        self,
        create_product_dto: CreateProductDTO,
        create_product_handler: Annotated[CreateProductHandler, Depends()],
        product_reader: Annotated[ProductReader, Depends()],
    ) -> ProductDTO:
        """Create product endpoint.

        :param product: Product DTO object
        :param product_reader: ProductReader depends object
        """
        product_id = await create_product_handler(create_product_dto)
        product = await product_reader.get_product_by_id(product_id)
        return product
