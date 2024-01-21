Simple order app

Run Docker:

Create `dev_config.yml` file in `config_dist` dir like this:

```yaml
db:
    type: postgresql
    connector: asyncpg
    host: localhost
    port: 5433
    user: order
    password: order
    database: order
```

Create .dev.env like this:

```
CONFIG_PATH=./config_dist/dev_config.yml
POSTGRES_HOST=localhost
POSTGRES_PORT=5433
POSTGRES_USER=order
POSTGRES_PASSWORD=order
POSTGRES_DB=order
```