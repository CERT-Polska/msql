from typing import Any, List
from typing_extensions import Protocol


class Cursor(Protocol):

    def execute(self, statement: str, *args: Any) -> None:
        ...

    def fetchone(self) -> Any:
        ...

    def fetchall(self) -> List[Any]:
        ...
