import pathlib
import frontmatter
from mdserver.var import ROOT_FOLDER

class BlogContent:
    def __init__(self, path:str):
        self.path = str(ROOT_FOLDER / path)
        self._raw:str = ''      # raw markdown content from file
        self.headers:dict = {}  # frontmatter metadata (headers)
        self.content:str = ''   # markdown content without frontmatter
        self._resolve_file_path()
        self._load_from_file()
        self._parse()
        
    def _resolve_file_path(self):
        # blog and folder index paths
        index_path = pathlib.Path(self.path) / 'index.md'
        blog_path = str(pathlib.Path(self.path)) + '.md'
        
        if index_path.exists():
            self.path = str(index_path)
        else:
            self.path = str(blog_path)

    def _load_from_file(self):
        #
        # load raw markdown content from file and store it in self._raw
        #
        # if fetching index file for a folder
        
        # if fetching actual blog post
        path = pathlib.Path(self.path)
        self._raw = path.read_text(encoding='utf-8')

    def _parse(self):
        #
        # parse frontmatter metadata from self._raw and store it in self.headers
        #
        post = frontmatter.load(self.path)
        self.headers = post.metadata
        self.content = post.content

    def _resolve_author(self):
        pass