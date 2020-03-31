import os
from unittest import TestCase

from src import Database


class TestPostgres(TestCase):

    def test_connect(self) -> None:
        host = os.getenv("POSTGRES_HOST", "localhost")
        username = os.getenv("POSTGRES_USER", "morm")
        password = os.getenv("POSTGRES_PASSWORD", "hunter2")
        database = os.getenv("POSTGRES_DB", "morm")
        self.db = PostgresDb(
            f"postgres://{username}:{password}@{host}/{database}")
        self.db.migrate()


class PostgresDb(Database):

    def __init__(self, conn_str: str) -> None:
        super().__init__(conn_str, "./migrations")
