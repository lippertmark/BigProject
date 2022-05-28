from abc import ABC, abstractmethod
from typing import Iterable, Tuple, List

from os import path


class BaseMap(ABC):
    @abstractmethod
    def __setitem__(self, key: str, value: int) -> None:
        ...

    @abstractmethod
    def __getitem__(self, key: str) -> int:
        ...

    @abstractmethod
    def __delitem__(self, key: str) -> None:
        ...

    @abstractmethod
    def __iter__(self) -> Iterable[Tuple[str, int]]:
        ...

    def __contains__(self, key: str) -> bool:
        ...

    def __eq__(self, other: 'BaseMap') -> bool:
        ...

    def __bool__(self) -> bool:
        ...

    @abstractmethod
    def __len__(self):
        ...

    def items(self) -> Iterable[Tuple[str, int]]:
        ...

    def values(self) -> Iterable[int]:
        ...

    def keys(self) -> Iterable[str]:
        ...

    @classmethod
    def fromkeys(cls, iterable, value=None) -> 'BaseMap':
        ...

    def update(self, other=None) -> None:
        ...

    def get(self, key, default=None):
        ...

    def pop(self, key, *args):
        ...

    def popitem(self):
        ...

    def setdefault(self, key, default=None):
        ...

    def clear(self):
        ...

    def write(self, path: str) -> None:
        for key, value in self:
            # write to file
            pass

    @classmethod
    def read(cls, path: str) -> 'BaseMap':
        # TODO finish implementation
        my_obj = cls()
        opened_file = ...
        for key, value in opened_file:
            my_obj[key] = value

        return my_obj
