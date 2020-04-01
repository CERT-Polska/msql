from unittest import TestCase
import os
from tests import TestDb


class TestSqliteFile(TestCase):

    def setUp(self) -> None:
        self.db = TestDb("sqlite://test.db")

    def tearDown(self) -> None:
        os.remove("test.db")

    def test_migrate(self) -> None:
        self.db.migrate()

    def test_migrate_twice(self) -> None:
        self.db.migrate()
        self.db.migrate()
