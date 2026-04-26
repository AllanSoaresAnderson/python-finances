from view_baggins_script import show_baggins

if __name__ == '__main__':
    from src.provider import register_file_use_case
    from dotenv import load_dotenv
    load_dotenv()
    from os import getenv
    path = getenv('REGISTER_BAGGINS_PATH')
    if path is None:
        raise ValueError('Please set REGISTER_BAGGINS_PATH environment variable')
    register_file_use_case().register(path)
    show_baggins()