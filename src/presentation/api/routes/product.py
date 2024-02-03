from litestar import get


@get("/product/all")
async def get_all_products() -> list:
    return []
