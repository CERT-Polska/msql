from __future__ import annotations
from typing import cast, Any
from typing_extensions import Protocol
from src.cursor import Cursor


class Connection(Protocol):

    def cursor(self) -> Cursor:
        ...

    def close(self) -> None:
        ...

    def commit(self) -> None:
        ...

    def __enter__(self) -> Connection:
        ...

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        ...


def connection(conn_str: str) -> Connection:
    """
    Main factory that creates connections.
    Depending on connection string it will use library to create actual connection.

    :raises RuntimeError if unsupported DB type is used in connection string
    """

    def conn_sqlite() -> Connection:
        from sqlite3 import connect
        # this transforms "sqlite://:memory:" => ":memory:"
        return cast(Connection, connect(conn_str[len('sqlite://'):]))

    def conn_postgres() -> Connection:
        from psycopg2 import connect
        conn = connect(conn_str)
        # small hack to unify APIs
        setattr(conn, "executescript", conn.execute)
        return cast(Connection, connect(conn_str))

    def conn_unknown() -> Connection:
        raise RuntimeError("Unsupported DB type in connection string")

    switcher = {"sqlite": conn_sqlite, "postgres": conn_postgres}
    db_type = conn_str.split(':')[0]

    return switcher.get(db_type, conn_unknown)()
