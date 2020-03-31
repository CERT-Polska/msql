from __future__ import annotations
from typing import List, Callable, Any

from src.connection import Connection, connection
from src.migration_tool import MigrationTool


def tolist(func: Callable[..., List]) -> Callable[..., List]:

    def wrapper(*args: Any, **kwargs: Any) -> List:
        return list(func(*args, **kwargs))

    return wrapper


class Database:

    def __init__(self,
                 conn_str: str,
                 migration_dir: str,
                 schema_table: str = "morm_migration") -> None:
        self.conn_str = conn_str
        self.migration_tool = MigrationTool(conn_str, migration_dir,
                                            schema_table)

    def migrate(self) -> None:
        self.migration_tool.install()

    def connection(self) -> Connection:
        return connection(self.conn_str)
