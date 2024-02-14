import asyncio
from pathlib import Path
from typing import AsyncGenerator

import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from src.infrastructure.db.config import DBConfig
from src.infrastructure.db.models.base import BaseModel
from src.infrastructure.db.models.product import Product
from src.presentation.api.config.parser import load_config
from src.presentation.api.di.db import build_async_engine


@pytest.fixture(scope='session')
def event_loop():
    """
    Creates an instance of the default event loop for the test session.
    """
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()

    try:
        yield loop
    finally:
        loop.close()


@pytest.fixture(name="path", scope="session")
def config_path() -> str:
    path = Path(__file__).parent / "utils/config/test_config.yml"
    return str(path)


@pytest.fixture(scope="session")
def db_config(path: str) -> DBConfig:
    return load_config(path, "db")


@pytest_asyncio.fixture(name="engine", scope="session")
async def create_engine(db_config: DBConfig) -> AsyncGenerator[AsyncEngine, None]:
    engine = await anext(build_async_engine(db_config))
    yield engine


@pytest_asyncio.fixture(scope="session")
async def tables(engine: AsyncEngine) -> AsyncGenerator[None, None]:
    async with engine.connect() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)
        await conn.commit()
        try:
            yield conn
        finally:
            await conn.run_sync(BaseModel.metadata.drop_all)


@pytest_asyncio.fixture(scope="function")
async def session(engine: AsyncEngine, tables: None) -> AsyncGenerator[AsyncSession, None]:
    async with engine.connect() as conn:
        transaction = await conn.begin()
        sessionmaker = async_sessionmaker(
            bind=conn,
            autoflush=False,
            expire_on_commit=False,
            autocommit=False,
            join_transaction_mode="create_savepoint",
        )
        async with sessionmaker() as session:
            yield session
        await transaction.rollback()


@pytest_asyncio.fixture
async def created_product(engine: AsyncEngine) -> Product:
    async with AsyncSession(engine) as session:
        product = Product(title="milk", price=0.5, weight=1000)

        session.add(product)
        await session.commit()
        await session.refresh(product)

        yield product

        session.delete(product)
        await session.commit()
