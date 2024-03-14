from dataclasses import dataclass, field

from dishka import Provider, Scope

from src.infrastructure.db import DBConfig
from src.infrastructure.log import LoggingConfig
from src.infrastructure.message_broker.config import EventBusConfig


@dataclass
class APIConfig:
    host: str = "127.0.0.1"
    port: int = 8000


@dataclass
class Config:
    db: DBConfig = field(default_factory=DBConfig)
    logging: LoggingConfig = field(default_factory=LoggingConfig)
    api: APIConfig = field(default_factory=APIConfig)
    event_bus: EventBusConfig = field(default_factory=EventBusConfig)


def setup_di_config(config: Config, main_provider: Provider) -> None:
    main_provider.provide(lambda: config, scope=Scope.APP, provides=Config)
    main_provider.provide(lambda: config.db, scope=Scope.APP, provides=DBConfig)
    main_provider.provide(lambda: config.logging, scope=Scope.APP, provides=LoggingConfig)
    main_provider.provide(lambda: config.api, scope=Scope.APP, provides=APIConfig)
    main_provider.provide(lambda: config.event_bus, scope=Scope.APP, provides=EventBusConfig)
