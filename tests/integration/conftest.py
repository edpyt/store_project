import os
from typing import Generator

import pytest
from alembic.command import upgrade
from alembic.config import Config as AlembicConfig
from litestar import Litestar
from litestar.testing import AsyncTestClient
from testcontainers.postgres import PostgresContainer
from testcontainers.rabbitmq import RabbitMqContainer

from src.presentation.api.main import init_api


@pytest.fixture(scope="session")
def rabbitmq_container() -> Generator[RabbitMqContainer, None, None]:
    container = RabbitMqContainer(
        "rabbitmq:3.13.0-alpine",
        username="test",
        password="test",
    )
    yield container.start()
    container.stop()


@pytest.fixture(scope="session")
def postgres_container() -> Generator[PostgresContainer, None, None]:
    container = PostgresContainer(
        "postgres:16-alpine",
        user="test",
        dbname="test",
        password="test",
    )

    yield container.start()
    container.stop()


@pytest.fixture(scope="session", name="alembic_config")
def create_alembic_config() -> AlembicConfig:
    alembic_config = AlembicConfig("alembic.ini")
    return alembic_config


@pytest.fixture(scope="session")
def run_db_migrations(alembic_config: AlembicConfig) -> None:
    upgrade(alembic_config, "head")


@pytest.fixture
async def test_client(
    postgres_container: PostgresContainer,
    rabbitmq_container: RabbitMqContainer,
):
    os.environ["POSTGRES_PORT"] = postgres_container.get_exposed_port("5432")
    os.environ["RMQ_PORT"] = rabbitmq_container.get_exposed_port("5672")
    os.environ["CONFIG_PATH"] = "./tests/utils/config/test_config.toml"

    app: Litestar = init_api()
    async with AsyncTestClient(app=app) as client:
        yield client