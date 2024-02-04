from litestar import get

from src.application.product import dto


@get("/product/all")
async def get_all_products() -> list[dto.ProductDTO]:
    return []
