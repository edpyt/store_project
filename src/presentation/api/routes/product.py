from litestar import get


@get("/product/all")
def get_all_products() -> None:
    return []
