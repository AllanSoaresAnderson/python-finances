from domain.interfaces import RegisterFileUseCase
from _provider import _register_file_use_case_impl

def register_file_use_case() -> RegisterFileUseCase:
    return _register_file_use_case_impl()
