from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.infrastructure.db.config import DBConfig


def build_sa_engine(db_config: DBConfig) -> AsyncEngine:
    engine = create_async_engine(db_config.full_url, echo=db_config.echo, pool_size=50)
    return engine


def build_sa_session_factory(
    engine: AsyncEngine,
) -> async_sessionmaker[AsyncSession]:
    session_factory = async_sessionmaker(
        bind=engine, autoflush=False, expire_on_commit=False
    )
    return session_factory


async def build_sa_session(
    session_factory: async_sessionmaker[AsyncSession],
) -> AsyncGenerator[AsyncSession, None]:
    async with session_factory() as session:
        yield session
