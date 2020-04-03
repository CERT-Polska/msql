import os
from typing import List, Optional
from unittest import TestCase
from tests import TestDb, Example


class PostgresTestDb(TestDb):

    def get_all_example(self) -> List[Example]:
        with self.get_cursor() as cursor:
            cursor.execute("SELECT * FROM example;")
            return [Example(*x) for x in cursor.fetchall()]

    def get_example_by_id(self, example_id: int) -> Optional[Example]:
        with self.get_cursor() as cursor:
            cursor.execute("SELECT * FROM example WHERE id = %s;", (example_id,))
            example = cursor.fetchone()
            if example:
                return Example(*example)
            else:
                return None

    def insert_example(self, example: Example) -> None:
        with self.get_cursor() as cursor:
            cursor.execute("INSERT INTO example (id, name) VALUES (%s, %s)", (
                example.id,
                example.name,
            ))

    def delete_example_by_id(self, example_id: int) -> None:
        with self.get_cursor() as cursor:
            cursor.execute("DELETE FROM example WHERE id = %s;", (example_id,))


class TestPostgres(TestCase):

    example0 = Example(0, "example0")
    example1 = Example(1, "example1")

    def setUp(self) -> None:
        host = os.getenv("POSTGRES_HOST", "localhost")
        username = os.getenv("POSTGRES_USER", "msql")
        password = os.getenv("POSTGRES_PASSWORD", "hunter2")
        database = os.getenv("POSTGRES_DB", "msql")
        self.db = PostgresTestDb(f"postgres://{username}:{password}@{host}/{database}")

    def tearDown(self) -> None:
        conn = self.db.connection()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE msql_migration,example;")
        conn.commit()

    def test_migrate(self) -> None:
        self.db.migrate()

    def test_migrate_twice(self) -> None:
        self.db.migrate()
        self.db.migrate()

    def test_select_empty(self) -> None:
        self.db.migrate()
        self.assertListEqual(self.db.get_all_example(), [])

    def test_insert(self) -> None:
        self.db.migrate()
        self.db.insert_example(self.example0)
        self.assertListEqual(self.db.get_all_example(), [self.example0])
        self.db.insert_example(self.example1)
        self.assertListEqual(self.db.get_all_example(), [self.example0, self.example1])

    def test_select_by_id(self) -> None:
        self.db.migrate()
        self.test_insert()
        self.assertEqual(self.db.get_example_by_id(self.example0.id), self.example0)

    def test_delete_by_id(self) -> None:
        self.db.migrate()
        self.test_insert()
        self.db.delete_example_by_id(self.example1.id)
        self.assertListEqual(self.db.get_all_example(), [self.example0])
