from morm import Database, Resource
from os import path


class BasicData:

    def __init__(self, basic_id: int, basic_name: str) -> None:
        self.id = basic_id
        self.name = basic_name


class BasicResource(Resource[BasicData]):
    TABLE = "basic"
    TABLE_ALIAS = "b"
    SELECT = "b.id, b.name"
    CLASS = BasicData


class BasicDb(Database):

    def __init__(self) -> None:
        # we can use any connection string here
        super().__init__("sqlite://:memory:", path.join(path.dirname(__file__), "migrations"))
        self.basic = BasicResource(self)

    def insert_basic(self, basic: BasicData) -> None:
        with self.connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO basic (
                id,
                name
            ) VALUES (
                ?,
                ?
            )""", (basic.id, basic.name,))
            conn.commit()

    def delete_basic(self, basic: BasicData) -> None:
        with self.connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
            DELETE FROM basic WHERE id = ?
            """, (basic.id,))
            conn.commit()