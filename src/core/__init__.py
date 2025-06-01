from typing import Self, Sequence


class QueryResult:
    def __init__(self, data: Sequence) -> None:
        self._data = data

    def __iter__(self) -> Self:
        self._len = len(self._data)
        self._curr = 0
        return self

    def __next__(self):
        if self._curr > self._len:
            raise StopIteration

        return self._data[self._curr]
