from unittest import TestCase

from src import Database


class TestSqlite(TestCase):

    def tearDown(self) -> None:
        ...

    def test_migrate_memory(self) -> None:
        self.db = SqliteDb("sqlite://:memory:")
        self.db.migrate()

    def test_migrate_file(self) -> None:
        self.db = SqliteDb("sqlite://test.db")
        self.db.migrate()


class SqliteDb(Database):

    def __init__(self, conn_str: str) -> None:
        super().__init__(conn_str, "./migrations")
