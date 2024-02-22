from di import bind_by_type
from di.dependent import Dependent
from didiator.interface.utils.di_builder import DiBuilder
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from src.infrastructure.db.main import build_sa_engine, build_sa_session_factory
from src.infrastructure.di.constants import DiScope


def setup_db_factories(di_builder: DiBuilder) -> None:
    di_builder.bind(
        bind_by_type(Dependent(build_sa_engine, scope=DiScope.APP), AsyncEngine)
    )
    di_builder.bind(
        bind_by_type(
            Dependent(build_sa_session_factory, scope=DiScope.APP),
            async_sessionmaker[AsyncSession],
        )
    )
