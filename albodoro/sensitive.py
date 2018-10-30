from collections import namedtuple

# stores sensitive data
secret_key = "&8qhbfs&+qj!2dtqnxh)j)vq9#)o)yo(il6^3h0pso$7ux48tp"
allowed_hosts = ("127.0.0.1", "localhost")

Postgres_settings = namedtuple("Postgres_settings", "name user password host port")
postgres_settings = Postgres_settings("", "", "", "", "")
