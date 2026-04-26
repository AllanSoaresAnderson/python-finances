from dotenv import load_dotenv

from application.csv_reader import CsvReaderImpl
from application.mapper.baggins_mapper import BagginsMapper
from application.mapper.entity_mapper import EntityMapper
from application.register_file_use_case import RegisterFileUseCaseImpl
from application.use_case.crud_file_use_case import CrudFileUseCaseImpl
from application.use_case.csv_writer import CsvWriterUseCaseImpl
from application.use_case.show_entities_in_file_use_case import ShowEntitiesInFileUseCaseImpl
from domain.enum import Table
from domain.interfaces import CsvReader, MapperUseCase, CrudFileUseCase, CrudRepository, BagginsRepository, \
    CsvWriterUseCase, EntityRepository
from infrastructure.repository.baggins_repository import BagginsRepositoryImpl
from infrastructure.repository.entity_repository import EntityRepositoryImpl

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


def _entity_mapper() -> EntityMapper:
    return EntityMapper()


def _mapper_use_case(table: Table) -> MapperUseCase:
    if table == Table.BAGGINS:
        return _baggins_mapper()

    if table == Table.ENTITY:
        return _entity_mapper()

    raise ValueError('Invalid table')


def _baggins_repository_impl():
    return BagginsRepositoryImpl(
        database=_database_connection_sqlite(),
    )


def _baggins_repository() -> BagginsRepository:
    return _baggins_repository_impl()


def _entity_repository_impl() -> EntityRepositoryImpl:
    return EntityRepositoryImpl(
        database=_database_connection_sqlite(),
    )


def _entity_repository() -> EntityRepository:
    return _entity_repository_impl()


def _crud_repository(table: Table) -> CrudRepository:
    if table == Table.BAGGINS:
        return _baggins_repository()

    if table == Table.ENTITY:
        return _entity_repository()

    raise ValueError('Invalid table')


def _crud_file_use_case_impl(table: Table) -> CrudFileUseCaseImpl:
    return CrudFileUseCaseImpl(
        repository=_crud_repository(table),
    )


def _crud_file_use_case(table: Table) -> CrudFileUseCase:
    return _crud_file_use_case_impl(table)


def _register_file_use_case_impl(table: Table) -> RegisterFileUseCaseImpl:
    return RegisterFileUseCaseImpl(
        reader=_csv_reader(),
        mapper=_mapper_use_case(table),
        repository=_crud_file_use_case(table),
    )


def _csv_writer_use_case_impl() -> CsvWriterUseCaseImpl:
    return CsvWriterUseCaseImpl()


def _csv_writer_use_case() -> CsvWriterUseCase:
    return _csv_writer_use_case_impl()


def _show_entities_in_file_use_case_impl(table: Table) -> ShowEntitiesInFileUseCaseImpl:
    return ShowEntitiesInFileUseCaseImpl(
        repository=_crud_repository(table),
        mapper=_mapper_use_case(table),
        writer=_csv_writer_use_case()
    )


if __name__ == '__main__':
    repository = _baggins_repository_impl()
    baggins = repository.find_all()

    for b in baggins:
        print(b)
