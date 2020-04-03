from src import BaseDb
from os import path


class TestDb(BaseDb):

    def __init__(self, conn_str: str) -> None:
        super().__init__(conn_str, path.join(path.dirname(__file__), "migrations"))
