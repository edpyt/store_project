from typing import Annotated

from dishka.integrations.litestar import FromDishka, inject
from litestar import Controller, get, post

from src.application.product.commands.create_product import (
    CreateProductHandler,
)
from src.application.product.dto.products import ProductDTO
from src.application.product.interfaces.persistence.reader import ProductReader
from src.presentation.api.dto.product import CreateProductDTO, ReturnProductDTO


class ProductController(Controller):
    path = "/product"
    tags = ["Product"]

    @get(
        "/all",
        summary="GET products",
        description="Get all products from database.",
    )
    @inject
    async def get_all_products(
        self,
        product_reader: Annotated[ProductReader, FromDishka()],
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
    )
    @inject
    async def create_product(
        self,
        create_product_dto: CreateProductDTO,
        create_product_handler: Annotated[CreateProductHandler, FromDishka()],
        product_reader: Annotated[ProductReader, FromDishka()],
    ) -> ProductDTO:
        """Create product endpoint.

        :param product: Product DTO object
        :param product_reader: ProductReader depends object
        """
        product_id = await create_product_handler(create_product_dto)
        product = await product_reader.get_product_by_id(product_id)
        return product
