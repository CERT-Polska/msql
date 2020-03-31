from typing_extensions import Protocol


class Transaction(Protocol):

    def rollback(self) -> None:
        ...

    def commit(self) -> None:
        ...
