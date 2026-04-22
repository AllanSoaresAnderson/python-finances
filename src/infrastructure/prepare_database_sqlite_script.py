
from src._provider import _prepare_database_sqlite
from src.domain.constants import DATABASE_SQLITE


if __name__ == '__main__':
    case = _prepare_database_sqlite()
    case.prepare(DATABASE_SQLITE)