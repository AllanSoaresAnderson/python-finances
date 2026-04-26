from abc import ABC, abstractmethod
from sqlite3 import Connection

class DatabaseConnectionSqlLite(ABC):
    """
    Abstract class that return a database connection of sqlite
    """

    @abstractmethod
    def get_connection(self) -> Connection:
        """
        Get a database connection of sqlite
        :return:
        """

class PrepareDataBaseSqlLite(ABC):

    @abstractmethod
    def prepare(self):
        pass

