import os
from unittest import TestCase
from tests import TestDb


class TestPostgres(TestCase):

    def test_connect(self) -> None:
        host = os.getenv("POSTGRES_HOST", "localhost")
        username = os.getenv("POSTGRES_USER", "morm")
        password = os.getenv("POSTGRES_PASSWORD", "hunter2")
        database = os.getenv("POSTGRES_DB", "morm")
        self.db = TestDb(
            f"postgres://{username}:{password}@{host}/{database}")
        self.db.migrate()
