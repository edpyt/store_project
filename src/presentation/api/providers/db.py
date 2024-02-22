from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.infrastructure.db.config import DBConfig


async def build_async_engine(
    db_config: DBConfig,
) -> AsyncGenerator[AsyncEngine, None]:
    engine = create_async_engine(db_config.full_url)
    try:
        yield engine
    finally:
        await engine.dispose()


async def db_async_session(engine: AsyncEngine) -> AsyncGenerator[AsyncSession, None]:
    session_factory = async_sessionmaker(
        bind=engine, autoflush=False, expire_on_commit=False,
    )

    async with session_factory() as session:
        yield session
