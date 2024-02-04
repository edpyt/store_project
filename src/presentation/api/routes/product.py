from litestar import get

from src.application.product import dto
from src.application.product.interfaces.persistence.reader import ProductReader


@get("/product/all")
async def get_all_products(product_reader: ProductReader) -> list[dto.ProductDTO]:
    return await product_reader.get_products()
