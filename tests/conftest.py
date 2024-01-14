from typing import AsyncGenerator

import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.infrastructure.db import build_async_engine
from src.infrastructure.db.config import DBConfig


@pytest.fixture
def db_config() -> DBConfig:
    return DBConfig(user='test', password='test')


@pytest_asyncio.fixture(scope='session')
async def engine(db_config: DBConfig) -> AsyncEngine:
    return build_async_engine(db_config.full_url)


@pytest_asyncio.fixture
async def session(
    engine: AsyncEngine
) -> AsyncGenerator[AsyncSession, None]:
    async with engine.begin() as session:
        yield session
