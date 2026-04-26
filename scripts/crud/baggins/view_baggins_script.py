

def show_baggins():
    from src.provider import show_entities_in_file_use_case
    from dotenv import load_dotenv
    load_dotenv()
    from os import getenv
    path = getenv('VIEW_BAGGINS_PATH')
    if path is None:
        raise ValueError('Please set VIEW_BAGGINS_PATH environment variable')

    show_entities_in_file_use_case().show(
        path=path,
    )



if __name__ == '__main__':
    show_baggins()