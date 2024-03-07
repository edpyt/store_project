from logging import Logger

from dishka import Provider, Scope, provide

from src.application.common.interfaces.uow import UnitOfWork
from src.infrastructure.log import build_logger
from src.infrastructure.uow import build_uow


class MainProvider(Provider):
    logger = provide(build_logger, scope=Scope.APP, provides=Logger)
    uow = provide(build_uow, scope=Scope.REQUEST, provides=UnitOfWork)
