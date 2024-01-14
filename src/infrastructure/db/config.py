from dataclasses import dataclass


@dataclass
class DBConfig:
    type: str = 'postgresql'
    connector: str | None = None
    host: str = 'localhost'
    port: int = 5431
    database: str = 'test'
    user: str = 'postgres'
    password: str = 'postgres'

    @property
    def full_url(self) -> str:
        if self.connector:
            dialect = f'{self.type}+{self.connector}'
        else:
            dialect = self.type

        database_url = '{}:{}@{}:{}/{}'.format(
            self.user,
            self.password,
            self.host,
            self.port,
            self.database
        )
        return dialect + '://' + database_url
