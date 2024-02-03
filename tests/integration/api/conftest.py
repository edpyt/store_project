from typing import AsyncGenerator

import pytest_asyncio
from litestar import Litestar
from litestar.testing import AsyncTestClient

from src.presentation.api.main import build_app


@pytest_asyncio.fixture
async def app() -> Litestar:
    return build_app()


@pytest_asyncio.fixture
async def client(app: Litestar) -> AsyncGenerator[AsyncTestClient, None]:
    async with AsyncTestClient(app=app) as ac:
        yield ac
