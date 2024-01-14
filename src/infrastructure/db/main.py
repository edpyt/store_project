from typing import AsyncGenerator
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio.engine import create_async_engine, AsyncEngine
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.infrastructure.db.config import DBConfig


@asynccontextmanager
async def build_async_engine(
    db_config: DBConfig
) -> AsyncGenerator[AsyncEngine, None]:
    engine = create_async_engine(db_config.full_url)
    try:
        yield engine
    finally:
        await engine.dispose()


@asynccontextmanager
async def db_async_session(
    engine: AsyncEngine
) -> AsyncGenerator[AsyncSession, None]:
    async with engine.begin() as session:
        yield session
