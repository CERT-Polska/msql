from __future__ import annotations
from typing import Any, Tuple, Optional, cast
from typing_extensions import Protocol
from src.cursor import Cursor
from src.transaction import Transaction


class Connection(Protocol):

    def cursor(self) -> Cursor:
        ...

    def begin(self) -> Transaction:
        ...

    def close(self) -> None:
        ...

    def execute(self,
                sql_statement: str,
                params: Optional[Tuple] = None) -> None:
        ...

    def executemany(self, sql_statement: str) -> None:
        ...

    def __enter__(self, *args: Any, **kwargs: Any) -> Connection:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.close()


def connection(conn_str: str) -> Connection:
    """
    Main factory that creates connections.
    Depending on connection string it will use library to create actual connection.

    :raises RuntimeError if unsupported DB type is used in connection string
    """

    def conn_sqlite() -> Connection:
        from sqlite3 import connect
        return cast(Connection, connect(conn_str))

    def conn_postgres() -> Connection:
        from psycopg2 import connect
        return cast(Connection, connect(conn_str))

    def conn_unknown() -> Connection:
        raise RuntimeError("Unsupported DB type in connection string")

    switcher = {"sqlite3": conn_sqlite, "postgres": conn_postgres}

    return switcher.get(conn_str.split(':')[0], conn_unknown)()
