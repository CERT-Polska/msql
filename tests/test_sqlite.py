from unittest import TestCase
from tests import TestDb


class TestSqlite(TestCase):

    def tearDown(self) -> None:
        ...

    def test_migrate_memory(self) -> None:
        self.db = TestDb("sqlite://:memory:")
        self.db.migrate()

    def test_migrate_file(self) -> None:
        self.db = TestDb("sqlite://test.db")
        self.db.migrate()

