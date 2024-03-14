from typing import AsyncGenerator

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from src.infrastructure.db.config import DBConfig
from src.infrastructure.db.main import (
    build_sa_engine,
    build_sa_session,
    build_sa_session_factory,
)


class DBProvider(Provider):
    @provide(scope=Scope.APP)
    async def sa_engine(self, db_config: DBConfig) -> AsyncGenerator[AsyncEngine, None]:
        engine = build_sa_engine(db_config)
        yield engine
        await engine.dispose()

    @provide(scope=Scope.APP)
    async def sa_session_factory(
        self, engine: AsyncEngine
    ) -> async_sessionmaker[AsyncSession]:
        return build_sa_session_factory(engine)

    @provide(scope=Scope.REQUEST)
    async def sa_session(
        self, sa_session_factory: async_sessionmaker[AsyncSession]
    ) -> AsyncGenerator[AsyncSession, None]:
        session = await anext(build_sa_session(sa_session_factory))
        yield session
