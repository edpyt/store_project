import os
from dataclasses import dataclass, field


@dataclass
class DBConfig:
    host: str = "localhost"
    port: int | str = field(
        default_factory=lambda: os.environ.get("POSTGRES_PORT", 5671)
    )
    database: str = "test"
    user: str = "postgres"
    password: str = "postgres"
    echo: bool = False

    @property
    def full_url(self) -> str:
        return "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
            self.user,
            self.password,
            self.host,
            self.port,
            self.database,
        )
