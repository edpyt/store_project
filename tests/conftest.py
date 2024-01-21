import os
from pathlib import Path
from typing import AsyncGenerator

import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.common.config.parser.main import load_config
from src.infrastructure.db import build_async_engine
from src.infrastructure.db.config import DBConfig


@pytest.fixture(name='path', scope='session')
def config_path() -> str:
    path: str | None = Path(__file__).parent / 'config/test_config.yml'
    return path


@pytest.fixture(scope='session')
def db_config(path: str) -> DBConfig:
    return load_config(path, 'db')  # type: ignore


@pytest_asyncio.fixture(scope='session')
async def engine(db_config: DBConfig) -> AsyncEngine:
    return await anext(build_async_engine(db_config))


@pytest_asyncio.fixture
async def session(
    engine: AsyncEngine
) -> AsyncGenerator[AsyncSession, None]:
    async with engine.begin() as session:
        yield session
