from typing import Annotated

from didiator import Mediator
from litestar import Controller, Response, get, post
from litestar.di import Provide
from litestar.params import Dependency

from src.application.product.commands.create_product import CreateProduct
from src.application.product.dto.products import ProductDTO
from src.application.product.interfaces.persistence.reader import ProductReader
from src.presentation.api.providers.product import create_product_reader_impl


class ProductController(Controller):  # type: ignore[misc]
    path = "/product"
    tags = ["Product"]

    dependencies: dict[str, Provide] = {
        "product_reader": Provide(create_product_reader_impl),
    }

    @get(
        "/all",
        summary="GET products",
        description="Get all products from database.",
    )  # type: ignore[misc]
    async def get_all_products(
        self,
        product_reader: Annotated[
            ProductReader, Dependency(skip_validation=True)
        ],
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
    )  # type: ignore[misc]
    async def create_product(  # type: ignore[empty-body]
        self,
        create_product_command: CreateProduct,
        mediator: Annotated[Mediator, Dependency(skip_validation=True)],
    ) -> Response:
        """Create product endpoint.

        :param product: Product DTO object
        :param product_reader: ProductReader depends object
        """
        product_id = await mediator.send(create_product_command)
        product = product_id
        # product = await mediator.query(GetProductById(product_id=product_id))
        return Response(product, status_code=201)
