from __future__ import annotations

from typing import List, Tuple
from unittest import TestCase
from msql.ext.pydantic import to_pydantic_model, to_pydantic_model_list
from pydantic import BaseModel


class Example(BaseModel):
    id: int
    name: str

    def __eq__(self, other: Example) -> bool:  # type: ignore
        return self.id == other.id and self.name == other.name


class TestPydantic(TestCase):

    def test_to_model(self) -> None:
        normal = Example(id=0, name="asd")
        converted = to_pydantic_model(Example, (
            0,
            "asd",
        ))
        self.assertEqual(normal, converted)

    def test_to_model_list(self) -> None:
        normal: List[Example] = []
        to_convert: List[Tuple] = []
        for i in range(5):
            normal.append(Example(id=i, name=str(i)))
            to_convert.append((i, str(i)))
        self.assertListEqual(to_pydantic_model_list(Example, to_convert), normal)
