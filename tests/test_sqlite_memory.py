from unittest import TestCase
from tests import TestDb


class TestSqliteMemory(TestCase):

    def setUp(self) -> None:
        self.db = TestDb("sqlite://:memory:")

    def test_migrate(self) -> None:
        self.db.migrate()

    def test_migrate_twice(self) -> None:
        self.db.migrate()
        self.db.migrate()
