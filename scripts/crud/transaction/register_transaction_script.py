from view_transaction_script import show_transaction
from domain.enum import Table

if __name__ == '__main__':
    from src.provider import register_file_use_case
    from dotenv import load_dotenv
    load_dotenv()
    from os import getenv
    path = getenv('REGISTER_TRANSACTION_PATH')
    if path is None:
        raise ValueError('Please set REGISTER_TRANSACTION_PATH environment variable')
    register_file_use_case(Table.TRANSACTION).register(path)
    show_transaction()