from src import Database
from os import path


class TestDb(Database):

    def __init__(self, conn_str: str) -> None:
        super().__init__(conn_str, path.join(path.dirname(__file__), "migrations"))
