from dataclasses import dataclass


@dataclass
class DBConfig:
    host: str = 'localhost'
    port: int = 5431
    database: str = 'test'
    user: str = ''
    password: str = ''

    @property
    def full_url(self) -> str:
        dialect = 'postgresql+asyncpg'
        database_url = '{}:{}@{}:{}/{}'.format(
            self.user,
            self.password,
            self.host,
            self.port,
            self.database
        )
        return dialect + '://' + database_url
