import os
from pathlib import Path
import jinja2
import markdown
import frontmatter
import json
import markdown.extensions.fenced_code, markdown.extensions.tables, markdown.extensions.admonition, markdown.extensions.codehilite
import flask

MD_EXTENSIONS = ['tables', 'fenced_code', 'admonition', 'pymdownx.tasklist']

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

def get_template(path:str) -> jinja2.Template:
    path = os.path.join(CONTENT_DIR, path)
    content = Path(path).read_text(encoding='utf-8')
    return jinja2.Template(content)

def parse_blog_frontmatter(content:str):
    return frontmatter.load(content)

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
    if path_exists(index_path) : return generate_page(index_path)

    # /blog/project/chapter.md
    split_path[-1] = split_path[-1] + '.md'
    blog_path = os.path.join(*split_path)
    if path_exists(blog_path) : return generate_page(blog_path)
    return generate_page('error/404.md'), 404


def get_author_info(name:str):
    user = {'name': None, 'avatar': None}
    try:
        with open(f'content/author/{name}.json') as file:
            loaded_data = json.loads(file.read())
            file.close()
        user['name'] = loaded_data.get('name')
        user['avatar'] = loaded_data.get('avatar')
        return user    
    except Exception as error:
        print(error)
        return user

def generate_blog_header(metadata:dict) -> str:
    """
    generate the post title + author header
    """
    title = metadata.get('title', 'Unnamed Blog Post')
    created_utc = metadata.get('created_utc', '-')
    updated_utc = metadata.get('updated_utc', '-')
    author = get_author_info(metadata.get('author'))
    author_name = author.get('name', 'Unknown Author')
    author_avatar = author.get('avatar', 'https://t4.ftcdn.net/jpg/11/26/55/79/360_F_1126557938_wxG9ULpFu2ZcuOVUVo6aM0QRfZVrgvqq.jpg')
    blog_template = get_template('file/blog_header.html')
    return blog_template.render(
        title=title, 
        author_name=author_name, 
        author_avatar=author_avatar, 
        created_utc=created_utc, 
        updated_utc=updated_utc if updated_utc else None
    )

def generate_page(path:str=None):
    try:
        path = os.path.join(CONTENT_DIR, path)
        with open(path, 'r+') as file:
            blog_md = file.read()
            file.close()
        
        post = frontmatter.loads(blog_md)
        blog_header_html = generate_blog_header(post.metadata)
        blog_md_html = markdown_to_html(post.content)
        autorefresh_js = Path(CONTENT_DIR, 'file/autoreload.js').read_text()
        blog_template = get_template('file/view_blog.html')
        return blog_template.render(header_html=blog_header_html, blog_html=blog_md_html, autorefresh_js=autorefresh_js)
    except FileNotFoundError:
        return generate_page('error/404.md')