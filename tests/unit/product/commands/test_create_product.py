from src.application.product.commands.create_product import CreateProductHandler
from tests.mocks.product_repo import ProductRepoMock
from tests.mocks.uow import UnitOfWorkMock


async def test_create_product_handler(
    product_repo: ProductRepoMock, uow: UnitOfWorkMock,
) -> None:
    handler = CreateProductHandler(product_repo, uow)  # noqa: F841
