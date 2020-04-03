from msql import BaseDb
from os import path
from typing import List, cast, Callable


class Basic:

    def __init__(self, basic_id: int, name: str) -> None:
        self.id = basic_id
        self.name = name


class Database(BaseDb):

    def __init__(self) -> None:
        # we can use any connection string here
        super().__init__("sqlite://:memory:", path.join(path.dirname(__file__), "migrations"))

    def select_all_basic(self) -> List[Basic]:
        with self.connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM basic")
            return cast(List[Basic], cursor.fetchall())

    def select_basic_by_id(self, basic_id: int) -> Basic:
        with self.connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM basic WHERE id = ?", (basic_id,))
            return cast(Basic, cursor.fetchone())

    def insert_basic(self, basic: Basic) -> None:
        with self.connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO basic (id, name) VALUES (?, ?)", (
                basic.id,
                basic.name,
            ))
            conn.commit()

    def update_basic(self, basic: Basic) -> None:
        with self.connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE basic SET name = ? WHERE id = ?", (
                basic.name,
                basic.id,
            ))
            conn.commit()

    def delete_basic_by_id(self, basic_id: int) -> None:
        with self.connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM basic WHERE id = ?", (basic_id,))
            conn.commit()
