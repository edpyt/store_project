import os
from typing import AsyncGenerator, Generator

import pytest
from alembic.config import Config as AlembicConfig
from litestar import Litestar
from litestar.testing import AsyncTestClient
from testcontainers.postgres import PostgresContainer

from src.infrastructure.db.config import DBConfig
from src.presentation.api.main import init_api
from tests.utils.init_db import migrate_db


@pytest.fixture(scope="session")
def postgres_container() -> Generator[PostgresContainer, None, None]:
    container = PostgresContainer(
        "postgres:16-alpine",
        5432,
        username="test",
        dbname="test",
        password="test",
    )

    yield container.start()
    container.stop()


@pytest.fixture(scope="session", name="db_config")
def create_db_config(
    postgres_container: PostgresContainer,
) -> Generator[DBConfig, None, None]:
    host = "localhost"
    port = postgres_container.get_exposed_port("5432")
    db_name = postgres_container.dbname
    user = postgres_container.username
    password = postgres_container.password

    db_config = DBConfig(host, port, db_name, user, password)
    yield db_config


@pytest.fixture(scope="session", name="alembic_config")
async def create_alembic_config() -> AsyncGenerator[AlembicConfig, None]:
    alembic_config = AlembicConfig("alembic.ini")
    yield alembic_config


# TODO: write transactional tests maybe
@pytest.fixture
async def run_db_migrations(
    db_config: DBConfig, alembic_config: AlembicConfig
) -> AsyncGenerator[None, None]:
    await migrate_db(db_config.full_url, alembic_config)
    yield


@pytest.fixture
async def test_client(
    postgres_container: PostgresContainer,
    run_db_migrations: None,
) -> AsyncGenerator[AsyncTestClient, None]:
    os.environ["POSTGRES_PORT"] = postgres_container.get_exposed_port("5432")
    os.environ["CONFIG_PATH"] = "./tests/utils/config/test_config.toml"

    app: Litestar = init_api()
    async with AsyncTestClient(app=app) as client:
        yield client
