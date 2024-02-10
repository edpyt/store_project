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


@pytest.fixture(name="path", scope="session")
def config_path() -> str:
    path = Path(__file__).parent / "utils/config/test_config.yml"
    return str(path)


@pytest.fixture(scope="session")
def db_config(path: str) -> DBConfig:
    return load_config(path, "db")  # type: ignore


@pytest_asyncio.fixture(name="engine", scope="function")
async def create_engine(db_config: DBConfig) -> AsyncEngine:
    engine = await anext(build_async_engine(db_config))

    yield engine
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)


@pytest_asyncio.fixture(autouse=True)
async def create_all(engine: AsyncEngine) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)


@pytest_asyncio.fixture
async def session(engine: AsyncEngine) -> AsyncGenerator[AsyncSession, None]:
    session_factory = async_sessionmaker(
        bind=engine, autoflush=False, expire_on_commit=False,
    )

    async with session_factory() as session:
        yield session


@pytest_asyncio.fixture
async def created_product(session: AsyncSession) -> Product:
    product = Product(title="milk", price=0.5, weight=1000)

    session.add(product)
    await session.commit()
    await session.refresh(product)

    return product
