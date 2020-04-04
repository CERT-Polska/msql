from __future__ import annotations

from msql import BaseDb
from os import path


class Example:

    def __init__(self, example_id: int, name: str) -> None:
        self.id = example_id
        self.name = name

    def __eq__(self, other: Example) -> bool:  # type: ignore
        return self.id == other.id and self.name == other.name


class TestDb(BaseDb):

    def __init__(self, conn_str: str) -> None:
        super().__init__(conn_str, path.join(path.dirname(__file__), "migrations"))
