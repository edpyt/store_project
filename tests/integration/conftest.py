from typing import AsyncGenerator, Generator

import pytest
from litestar import Litestar
from litestar.testing import AsyncTestClient
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from testcontainers.postgres import PostgresContainer

from src.infrastructure.db.models import BaseModel
from src.presentation.api.main import init_api


@pytest.fixture(scope="session")
def postgres_container() -> Generator[PostgresContainer, None, None]:
    container = PostgresContainer("postgres:16-alpine")
    yield container.start()
    container.stop()


@pytest.fixture(name="postgres_url", scope="session")
def get_postgres_url(
    postgres_container: PostgresContainer,
) -> Generator[str, None, None]:
    postgres_url = postgres_container.get_connection_url().replace(
        "postgresql+psycopg2", "postgresql+asyncpg"
    )
    yield postgres_url


@pytest.fixture(name="session_factory")
async def create_session_factory(
    postgres_url: str,
) -> AsyncGenerator[async_sessionmaker[AsyncSession], None]:
    engine = create_async_engine(url=postgres_url)
    BaseModel.metadata.create_all(engine)
    session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
        bind=engine, expire_on_commit=False, autoflush=False
    )
    yield session_factory
    await engine.dispose()
    BaseModel.metadata.create_all(engine)


@pytest.fixture(name="session")
async def create_session(
    session_factory: async_sessionmaker[AsyncSession],
) -> AsyncGenerator[AsyncSession, None]:
    async with session_factory() as session:
        yield session


@pytest.fixture
async def test_client(container: PostgresContainer):
    app: Litestar = init_api()
    async with AsyncTestClient(app=app) as client:
        yield client
