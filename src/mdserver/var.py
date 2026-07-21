from dotenv import load_dotenv; load_dotenv()
import os
import pathlib
    
path = os.environ.get('CONTENT_PATH', '')
print(f'\n\n\n{path}\n\n\n')
ROOT_FOLDER:pathlib.Path   = pathlib.Path(path)
STATIC_FOLDER:pathlib.Path = ROOT_FOLDER / 'static'
AUTHOR_FOLDER:pathlib.Path = ROOT_FOLDER / 'author'