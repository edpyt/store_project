from typing import Annotated

from litestar import get
from litestar.di import Provide
from litestar.params import Dependency

from src.application.product import dto
from src.application.product.interfaces.persistence.reader import ProductReader
from src.infrastructure.db.repositories.product import (
    create_product_reader_impl,
)


@get(
    "/product/all",
    dependencies={"product_reader": Provide(create_product_reader_impl)},
)
async def get_all_products(
    product_reader: Annotated[ProductReader, Dependency(skip_validation=True)],
) -> list[dto.ProductDTO]:
    return await product_reader.get_products()
