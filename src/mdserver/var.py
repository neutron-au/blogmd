from dotenv import load_dotenv; load_dotenv()
import os
import pathlib
    

DEBUG:bool   = bool(os.environ.get('DEBUG', 'false').lower() == 'true')

path = os.environ.get('CONTENT_PATH', 'content')
ROOT_FOLDER:pathlib.Path   = pathlib.Path(path)
STATIC_FOLDER:pathlib.Path = ROOT_FOLDER / 'static'
AUTHOR_FOLDER:pathlib.Path = ROOT_FOLDER / 'author'