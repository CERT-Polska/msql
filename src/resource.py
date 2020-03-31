from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import List, TypeVar, Generic, Optional, Tuple, cast

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.database import Database

T = TypeVar("T")


class Resource(Generic[T], metaclass=ABCMeta):

    def __init__(self, db: Database) -> None:
        self._db = db

    @property
    @abstractmethod
    def CLASS(self) -> type:
        raise NotImplementedError()

    @property
    @abstractmethod
    def SELECT(self) -> str:
        raise NotImplementedError()

    @property
    @abstractmethod
    def TABLE(self) -> str:
        raise NotImplementedError()

    @property
    @abstractmethod
    def TABLE_ALIAS(self) -> str:
        raise NotImplementedError()

    def select(self,
               suffix: str = "",
               params: Tuple = (),
               mod: str = "") -> List[T]:
        result = []
        with self._db.connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT {} {} FROM {} {} {}".format(mod, self.SELECT,
                                                    self.TABLE,
                                                    self.TABLE_ALIAS, suffix),
                params,
            )
            for row in cursor.fetchall():
                result.append(self.CLASS(*row))
        return result

    def select_distinct(self, suffix: str = "", params: Tuple = ()) -> List[T]:
        return self.select(suffix, params, mod="DISTINCT")

    def select_one(self, suffix: str = "", params: Tuple = ()) -> T:
        result = self.select_one_or_none(suffix, params)
        if not result:
            raise RuntimeError(f"Query on {self.TABLE} returned zero results")
        return result

    def select_one_or_none(self,
                           suffix: str = "",
                           params: Tuple = ()) -> Optional[T]:
        with self._db.connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT {} FROM {} {} {}".format(self.SELECT, self.TABLE,
                                                 self.TABLE_ALIAS, suffix),
                params,
            )
            result = cursor.fetchone()
            if not result:
                return None
            return cast(T, self.CLASS(*result))
