import markdown.extensions.fenced_code, markdown.extensions.tables, markdown.extensions.admonition, markdown.extensions.codehilite
from pymdownx import emoji, mark, highlight, arithmatex
import pathlib

MD_EXTENSIONS = [
    'tables', 'fenced_code', 'admonition', 'toc',
    'pymdownx.tasklist', 'pymdownx.caret', 'pymdownx.mark',
    'pymdownx.smartsymbols', 'pymdownx.magiclink', 'pymdownx.saneheaders',
    'pymdownx.emoji', 'pymdownx.keys', 'pymdownx.superfences', 'pymdownx.highlight',
    'pymdownx.arithmatex'
]

MD_EXTENSION_CONFIGS = {
    'pymdownx.emoji': {
        'emoji_index': emoji.gemoji,
        'emoji_generator': emoji.to_alt
    },
}

class RenderedMarkdown:
    def __init__(self, path:str=None, content:str=None):
        self.output:str = ''  # rendered html content
        self._path = path
        self._md_content = content

        if path:
            self._load_markdown_from_file()
        self._render()

    def __str__(self):
        return str(self._render())

    def _load_markdown_from_file(self):
        #
        # Read markdown file from disk and store it in 
        #
        self._md_content = pathlib.Path(self._path).read_text('utf-8')

    def _render(self) -> str:
        #
        # render markdown and save to self.output
        #
        print(self._md_content)
        self.output = markdown.markdown(self._md_content, extensions=MD_EXTENSIONS, extension_configs=MD_EXTENSION_CONFIGS)
        return self.output