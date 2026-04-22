from src.infrastructure.database.sql_lite_connection import SqlLiteConnection
from src.infrastructure.interfaces import PrepareDataBaseSqlLite, DatabaseConnectionSqlLite
from src.infrastructure.prepare_database_sqlite import PrepareDataBaseSqlLiteImpl


def _sqlite_connection() -> SqlLiteConnection:
    return SqlLiteConnection()


def _database_connection_sqlite() -> DatabaseConnectionSqlLite:
    return _sqlite_connection()


def _prepare_database_sqlite_impl() -> PrepareDataBaseSqlLiteImpl:
    return PrepareDataBaseSqlLiteImpl(
        database=_database_connection_sqlite()
    )


def _prepare_database_sqlite() -> PrepareDataBaseSqlLite:
    return _prepare_database_sqlite_impl()