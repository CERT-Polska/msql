from msql import BaseDb, Connection, Cursor
from os import path
from typing import List


class Basic:

    def __init__(self, basic_id: int, name: str) -> None:
        self.id = basic_id
        self.name = name


class Database(BaseDb):

    def __init__(self) -> None:
        # we can use any connection string here
        super().__init__("sqlite://:memory:", path.join(path.dirname(__file__), "migrations"))

    @BaseDb.with_cursor
    def select_all_basic(self, cursor: Cursor) -> List[Basic]:
        cursor.execute("SELECT * FROM basic")
        return [Basic(**x) for x in cursor.fetchall()]

    def select_basic_by_id(self, basic_id: int) -> Basic:
        with self.get_cursor() as cursor:
            cursor.execute("SELECT * FROM basic WHERE id = ?", (basic_id,))
            return Basic(**cursor.fetchone())

    def insert_basic(self, basic: Basic) -> None:
        with self.get_cursor() as cursor:
            cursor.execute("INSERT INTO basic (id, name) VALUES (?, ?)", (
                basic.id,
                basic.name,
            ))

    @BaseDb.with_cursor
    def update_basic(self, basic: Basic, cursor: Cursor) -> None:
        cursor.execute("UPDATE basic SET name = ? WHERE id = ?", (
            basic.name,
            basic.id,
        ))

    @BaseDb.with_cursor
    def delete_basic_by_id(self, basic_id: int, cursor: Connection) -> None:
        cursor.execute("DELETE FROM basic WHERE id = ?", (basic_id,))
