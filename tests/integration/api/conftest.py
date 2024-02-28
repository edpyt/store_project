from typing import AsyncGenerator

import pytest_asyncio
from litestar import Litestar
from litestar.testing import AsyncTestClient
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.product import dto
from src.infrastructure.db.models.product import Product
from src.presentation.api.main import init_api
from tests.utils.di import setup_test_di


@pytest_asyncio.fixture
async def app(path: str) -> AsyncGenerator[Litestar, None]:
    app: Litestar = init_api()
    setup_test_di(app, path)
    yield app


@pytest_asyncio.fixture
async def client(
    app: Litestar, tables: None,
) -> AsyncGenerator[AsyncTestClient, None]:
    async with AsyncTestClient(app=app) as ac:
        yield ac


@pytest_asyncio.fixture
async def created_product_dto(
    app: Litestar, session: AsyncSession, created_product: Product,
) -> AsyncGenerator[dto.ProductDTO, None]:
    # Using same session for test client and created product
    app.dependencies["session"] = lambda: session

    yield dto.ProductDTO(
        title=created_product.title,
        price=created_product.price,
        weight=created_product.weight,
    )  # type: ignore
