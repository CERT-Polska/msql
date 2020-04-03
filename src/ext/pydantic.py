import logging
from typing import Tuple, TypeVar, List, Dict, Any, Type

try:
    from pydantic import BaseModel
except ModuleNotFoundError:
    logging.exception("missing pydantic, please install using msql[pydantic]")

T = TypeVar("T", bound=BaseModel)


def to_pydantic_model(schema: Type[T], data: Tuple) -> T:
    ret: Dict[str, Any] = {}
    for index, key in enumerate(schema.__fields__):
        ret[key] = data[index]
    return schema(**ret)


def to_pydantic_model_list(schema: Type[T], data: List[Tuple]) -> List[T]:
    return [to_pydantic_model(schema, x) for x in data]
