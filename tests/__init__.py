from typing import List, cast

from src import BaseDb
from os import path


class Example:

    def __init__(self, example_id: int, name: str) -> None:
        self.id = example_id
        self.name = name


class TestDb(BaseDb):

    def __init__(self, conn_str: str) -> None:
        super().__init__(conn_str, path.join(path.dirname(__file__), "migrations"))
