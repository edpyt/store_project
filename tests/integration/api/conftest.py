from typing import AsyncGenerator

import pytest_asyncio
from litestar import Litestar
from litestar.testing import AsyncTestClient

from src.application.product import dto
from src.infrastructure.db.models.product import Product
from src.presentation.api.main import build_app
from tests.utils.di import setup_test_di


@pytest_asyncio.fixture
async def app() -> Litestar:
    return build_app()


@pytest_asyncio.fixture
async def client(
    app: Litestar, path: str,
) -> AsyncGenerator[AsyncTestClient, None]:
    setup_test_di(app, path)
    async with AsyncTestClient(app=app) as ac:
        yield ac


@pytest_asyncio.fixture
async def created_product_dto(created_product: Product) -> dto.ProductDTO:
    return dto.ProductDTO(
        title=created_product.title,
        price=created_product.price,
        weight=created_product.weight,
    )  # type: ignore
