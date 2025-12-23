import os
import jinja2
import markdown
import markdown.extensions.fenced_code, markdown.extensions.tables, markdown.extensions.admonition, markdown.extensions.codehilite
import flask

MD_EXTENSIONS = ['tables', 'fenced_code', 'admonition', 'codehilite']

CONTENT_DIR = 'content'

def path_exists(path:str=None):
    return os.path.exists(os.path.join(CONTENT_DIR, path))

def make_default_dirs():
    dirs = [
        os.path.join(CONTENT_DIR),
        os.path.join(CONTENT_DIR, 'blog'),
        os.path.join(CONTENT_DIR, 'error'),
        os.path.join(CONTENT_DIR, 'file'),
    ]
    for dir in dirs: os.makedirs(dir, exist_ok=True)

def get_template(path:str=None) -> jinja2.Template:
    if path == None : raise Exception('path value must not be None')
    path = os.path.join(CONTENT_DIR, path)
    with open(path, "r+") as file:
        content = file.read()
        file.close()
    return jinja2.Template(content)

def markdown_to_html(content:str=None):
    if content == None : raise Exception('content value must not be None')
    return markdown.markdown(content, extensions=MD_EXTENSIONS)

def send_file_raw(path:str=None):
    path = os.path.join(CONTENT_DIR, path)
    return flask.send_file(path)


def get_blog_page(path:str=None):
    split_path = list(filter(None, path.split('/')))
    # /blog/project/chapter/index.md
    index_path = os.path.join(*split_path, 'index.md')
    if path_exists(index_path) : return generate_page(index_path) ; print('INDEX PAGE EXISTS')
    # /blog/project/chapter.md
    split_path[-1] = split_path[-1] + '.md'
    blog_path = os.path.join(*split_path)
    if path_exists(blog_path) : return generate_page(blog_path) ; print('BLOG PAGE EXISTS')
    return generate_page('error/404.md')


def generate_page(path:str=None):
    try:
        path = os.path.join(CONTENT_DIR, path)
        with open(path, 'r+') as file:
            blog_md = file.read()
            file.close()
        blog_md_html = markdown_to_html(blog_md)
        blog_template = get_template('file/view_blog.html')
        return blog_template.render(blog_html=blog_md_html)
    except FileNotFoundError:
        return generate_page('error/404.md')