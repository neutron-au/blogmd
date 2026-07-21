import pathlib
import frontmatter
from mdserver.var import ROOT_FOLDER

class BlogContent:
    def __init__(self, path:str):
        self.path = str(ROOT_FOLDER / path) + '.md'
        self._raw:str = ''      # raw markdown content from file
        self.headers:dict = {}  # frontmatter metadata (headers)
        self.content:str = ''   # markdown content without frontmatter
        self._load_from_file()
        self._parse()

    def _load_from_file(self):
        #
        # load raw markdown content from file and store it in self._raw
        #
        self._raw = pathlib.Path(self.path).read_text(encoding='utf-8')

    def _parse(self):
        #
        # parse frontmatter metadata from self._raw and store it in self.headers
        #
        post = frontmatter.load(self.path)
        self.headers = post.metadata
        self.content = post.content