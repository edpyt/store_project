from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from src.infrastructure.db.main import (
    build_sa_engine,
    build_sa_session,
    build_sa_session_factory,
)


class DBProvider(Provider):
    sa_engine = provide(build_sa_engine, scope=Scope.APP, provides=AsyncEngine)
    sa_session_factory = provide(
        build_sa_session_factory,
        scope=Scope.APP,
        provides=async_sessionmaker[AsyncSession],
    )
    sa_session = provide(
        build_sa_session, scope=Scope.REQUEST, provides=AsyncSession
    )
