from view_entity_script import show_entity
from domain.enum import Table

if __name__ == '__main__':
    from src.provider import register_file_use_case
    from dotenv import load_dotenv
    load_dotenv()
    from os import getenv
    path = getenv('REGISTER_ENTITY_PATH')
    if path is None:
        raise ValueError('Please set REGISTER_ENTITY_PATH environment variable')
    register_file_use_case(Table.ENTITY).register(path)
    show_entity()