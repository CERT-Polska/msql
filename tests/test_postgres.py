import os
from unittest import TestCase
from tests import TestDb


class TestPostgres(TestCase):

    def setUp(self) -> None:
        host = os.getenv("POSTGRES_HOST", "localhost")
        username = os.getenv("POSTGRES_USER", "morm")
        password = os.getenv("POSTGRES_PASSWORD", "hunter2")
        database = os.getenv("POSTGRES_DB", "morm")
        self.db = TestDb(
            f"postgres://{username}:{password}@{host}/{database}")

    def tearDown(self) -> None:
        conn = self.db.connection()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE morm_migration,binaries;")

    def test_migrate(self) -> None:
        self.db.migrate()

    def test_migrate_twice(self) -> None:
        self.db.migrate()
        self.db.migrate()
