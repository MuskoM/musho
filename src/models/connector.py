from abc import ABC
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core import QueryResult


class ConnectorException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Connector(ABC):
    def __init__(self) -> None:
        self.name = self.__class__.__name__

    def query(self) -> QueryResult: ...
    def save(self) -> None: ...


class SQLConnector(Connector):
    def __init__(self, source: str) -> None:
        super().__init__()
        connector_db_engine = create_engine(source)
        self._session = sessionmaker(connector_db_engine)

    def query(self) -> QueryResult: ...
    def save(self) -> None: ...


class FileConnector(Connector):
    def __init__(self, source: str) -> None:
        super().__init__()
        self._root_path = Path(source)

        if not self._root_path.is_dir():
            raise ConnectorException("Incorrect base path, should be a directory.")

    def query(self) -> QueryResult: ...
    def save(self) -> None: ...
