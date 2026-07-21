import json
from mdserver.var import AUTHOR_FOLDER

class BlogAuthor:
    def __init__(self, name:str):
        self.name = name
        self.avatar:str = ''
        self._load_author_info()

    def _load_author_info(self) -> dict:
        author_file = AUTHOR_FOLDER / f'{self.name}.json'
        if author_file.exists():
            content = author_file.read_text(encoding='utf-8')
            data = json.loads(content)
            self.avatar = data.get('avatar', None)
        else:
            print('author does not exist!!!')
        return {}