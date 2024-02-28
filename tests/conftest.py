import asyncio
from pathlib import Path
from typing import AsyncGenerator

import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from src.infrastructure.config_loader import load_config
from src.infrastructure.db.config import DBConfig
from src.infrastructure.db.models.base import BaseModel
from src.infrastructure.db.models.product import Product
from src.presentation.api.providers.db import build_async_engine


@pytest.fixture(scope="session")
def event_loop():
    """Creates an instance of the default event loop for the test session."""
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()

    try:
        yield loop
    finally:
        loop.close()


@pytest.fixture(name="path", scope="session")
def config_path() -> Path:
    path = Path(__file__).parent / "utils/config/test_config.toml"
    return path


@pytest.fixture(scope="session")
def db_config(path: Path) -> DBConfig:
    return load_config(DBConfig, config_scope="db", path=str(path))


@pytest_asyncio.fixture(name="engine")
async def create_engine(
    db_config: DBConfig,
) -> AsyncGenerator[AsyncEngine, None]:
    engine = await anext(build_async_engine(db_config))
    yield engine


@pytest_asyncio.fixture
async def tables(engine: AsyncEngine) -> AsyncGenerator[None, None]:
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)
    yield conn
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)


@pytest_asyncio.fixture(scope="function")
async def session(
    engine: AsyncEngine, tables: None
) -> AsyncGenerator[AsyncSession, None]:
    sessionmaker = async_sessionmaker(
        bind=engine,
        autoflush=False,
        expire_on_commit=False,
        autocommit=False,
    )
    async with sessionmaker() as session:
        yield session


@pytest_asyncio.fixture
async def created_product(session: AsyncSession) -> Product:
    product = Product(title="milk", price=0.5, weight=1000)

    session.add(product)
    await session.commit()
    await session.refresh(product)

    yield product
