import os
from pathlib import Path
from typing import AsyncGenerator

import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.common.config.models.main import Config
from src.common.config.parser.main import load_config
from src.infrastructure.db import build_async_engine
from src.infrastructure.db.config import DBConfig


@pytest.fixture(name='path', scope='session')
def config_path() -> str:
    path: str | None = os.getenv('CONFIG_PATH')

    assert path, 'Not found CONFIG_PATH environment'

    return path


@pytest.fixture(scope='session')
def config(path: str) -> Config:
    return load_config(path)


@pytest.fixture(scope='session')
def db_config() -> DBConfig:
    return DBConfig(user='test', password='test')


@pytest_asyncio.fixture(scope='session')
async def engine(db_config: DBConfig) -> AsyncEngine:
    return build_async_engine(db_config)


@pytest_asyncio.fixture
async def session(
    engine: AsyncEngine
) -> AsyncGenerator[AsyncSession, None]:
    async with engine.begin() as session:
        yield session
