import os
from pathlib import Path
import flask
import pathlib
import markdown.extensions.fenced_code, markdown.extensions.tables, markdown.extensions.admonition, markdown.extensions.codehilite
from pymdownx import emoji, mark, highlight, arithmatex

from mdserver.var import ROOT_FOLDER, STATIC_FOLDER, AUTHOR_FOLDER

from mdserver.models import BlogContent, RenderedTemplate, RenderedMarkdown

def make_default_dirs():
    dirs = [
        ROOT_FOLDER / 'blog',
        ROOT_FOLDER / 'error',
        STATIC_FOLDER,
    ]
    for dir in dirs: os.makedirs(dir, exist_ok=True)

def send_file_raw(path:str=None):
    path = os.path.join(ROOT_FOLDER, path)
    return flask.send_file(path)

def send_blog_page(path:str=None):
    path = str(ROOT_FOLDER / path)

    # load template
    template = RenderedTemplate(STATIC_FOLDER / 'blog_post.html')
    
    blog_data         = BlogContent(path=path)
    blog_body_html    = RenderedMarkdown(content=blog_data.content).output
    blog_headers_html = RenderedMarkdown(content=blog_data.headers).output

    template.add_content('title', blog_data.headers.get('title', 'Unnamed Blog Post'))
    template.add_content('blog_html', RenderedMarkdown(content=blog_data.content).output)

    template._render()
    return template.output


