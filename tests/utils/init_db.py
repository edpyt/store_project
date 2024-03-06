from alembic.command import upgrade
from alembic.config import Config as AlembicConfig
from sqlalchemy.ext.asyncio import AsyncConnection, create_async_engine


async def migrate_db(conn_url: str, cfg: AlembicConfig) -> None:
    async_engine = create_async_engine(conn_url)
    async with async_engine.begin() as conn:
        await conn.run_sync(__execute_upgrade, cfg)


def __execute_upgrade(connection: AsyncConnection, cfg: AlembicConfig) -> None:
    cfg.attributes["connection"] = connection
    upgrade(cfg, "head")
