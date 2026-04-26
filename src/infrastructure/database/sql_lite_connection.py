from sqlite3 import Connection, connect

from src.infrastructure.interfaces import DatabaseConnectionSqlLite


class SqlLiteConnection(DatabaseConnectionSqlLite):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def get_connection(self) -> Connection:
        return connect(self.db_path)