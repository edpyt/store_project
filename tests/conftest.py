from pathlib import Path
from typing import AsyncGenerator

import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from src.application.common.config.parser import load_config
from src.infrastructure.db.config import DBConfig
from src.infrastructure.db.main import build_async_engine
from src.infrastructure.db.models.base import BaseModel


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
    
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)
    yield engine
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)


@pytest_asyncio.fixture
async def session(engine: AsyncEngine) -> AsyncGenerator[AsyncSession, None]:
    session_factory = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

    async with session_factory() as session:
        yield session
