from domain.enum import Table
from domain.interfaces import RegisterFileUseCase, ShowEntitiesInFileUseCase
from _provider import (
    _register_file_use_case_impl,
    _show_entities_in_file_use_case_impl,
)

def register_file_use_case(table: Table) -> RegisterFileUseCase:
    return _register_file_use_case_impl(table)


def show_entities_in_file_use_case(table: Table) -> ShowEntitiesInFileUseCase:
    return _show_entities_in_file_use_case_impl(table)