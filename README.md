Simple order app

Setup Docker:

Create `dev_config.yml` file in `config_dist` dir like this:

```yaml
db:
    type: postgresql
    connector: asyncpg
    host: localhost  # POSTGRES_HOST
    port: 5433  # POSTGRES_PORT
    user: order  # POSTGRES_USER
    password: order  # POSTGRES_PASSWORD
    database: order  # POSTGRES_DB
```

Update .dev.env and use variables from `dev_config.yml`, like this:

```
CONFIG_PATH=./config_dist/dev_config.yml
POSTGRES_HOST=localhost
POSTGRES_PORT=5433
POSTGRES_USER=order
POSTGRES_PASSWORD=order
POSTGRES_DB=order
```

Run tests:

```bash
make test
```