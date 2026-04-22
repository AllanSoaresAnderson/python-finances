from abc import ABC, abstractmethod
from sqlite3 import Connection

class DatabaseConnectionSqlLite(ABC):
    """
    Abstract class that return a database connection of sqlite
    """

    @abstractmethod
    def get_connection(self, database: str) -> Connection:
        """
        Get a database connection of sqlite
        :param database:
        :return:
        """

class PrepareDataBaseSqlLite(ABC):

    @abstractmethod
    def prepare(self, database: str):
        pass