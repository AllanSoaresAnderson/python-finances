from sqlite3 import Connection, connect

from src.infrastructure.interfaces import DatabaseConnectionSqlLite


class SqlLiteConnection(DatabaseConnectionSqlLite):

    def get_connection(self, database: str) -> Connection:
        return connect(database)