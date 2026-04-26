from dotenv import load_dotenv

from application.csv_reader import CsvReaderImpl
from application.mapper.baggins_mapper import BagginsMapper
from application.register_file_use_case import RegisterFileUseCaseImpl
from application.use_case.crud_file_use_case import CrudFileUseCaseImpl
from domain.interfaces import CsvReader, MapperUseCase, CrudFileUseCase, CrudRepository, BagginsRepository
from infrastructure.repository.baggins_repository import BagginsRepositoryImpl

load_dotenv()
from os import getenv

from src.infrastructure.database.sql_lite_connection import SqlLiteConnection
from src.infrastructure.interfaces import PrepareDataBaseSqlLite, DatabaseConnectionSqlLite
from src.infrastructure.prepare_database_sqlite import PrepareDataBaseSqlLiteImpl


def _sqlite_connection() -> SqlLiteConnection:
    path = getenv("DATABASE_SQLITE")
    if not path:
        raise ValueError("DATABASE_SQLITE environment variable not set")

    return SqlLiteConnection(db_path=path)


def _database_connection_sqlite() -> DatabaseConnectionSqlLite:
    return _sqlite_connection()


def _prepare_database_sqlite_impl() -> PrepareDataBaseSqlLiteImpl:
    return PrepareDataBaseSqlLiteImpl(
        database=_database_connection_sqlite()
    )


def _prepare_database_sqlite() -> PrepareDataBaseSqlLite:
    return _prepare_database_sqlite_impl()


def _csv_reader_impl() -> CsvReaderImpl:
    return CsvReaderImpl()


def _csv_reader() -> CsvReader:
    return _csv_reader_impl()


def _baggins_mapper() -> BagginsMapper:
    return BagginsMapper()


def _mapper_use_case() -> MapperUseCase:
    return _baggins_mapper()


def _baggins_repository_impl():
    return BagginsRepositoryImpl(
        database=_database_connection_sqlite(),
    )


def _baggins_repository() -> BagginsRepository:
    return _baggins_repository_impl()


def _crud_repository() -> CrudRepository:
    return _baggins_repository()


def _crud_file_use_case_impl() -> CrudFileUseCaseImpl:
    return CrudFileUseCaseImpl(
        repository=_crud_repository(),
    )


def _crud_file_use_case() -> CrudFileUseCase:
    return _crud_file_use_case_impl()


def _register_file_use_case_impl() -> RegisterFileUseCaseImpl:
    return RegisterFileUseCaseImpl(
        reader=_csv_reader(),
        mapper=_mapper_use_case(),
        repository=_crud_file_use_case(),
    )


if __name__ == '__main__':
    repository = _baggins_repository_impl()
    baggins = repository.find_all()

    for b in baggins:
        print(b)
