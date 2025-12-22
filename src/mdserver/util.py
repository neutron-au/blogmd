import os
import jinja2
import markdown
import flask

CONTENT_DIR = 'content'

def get_template(path:str=None) -> jinja2.Template:
    if path == None : raise Exception('path value must not be None')
    path = os.path.join(CONTENT_DIR, path)
    with open(path, "r+") as file:
        content = file.read()
        file.close()
    return jinja2.Template(content)

def markdown_to_html(content:str=None):
    if content == None : raise Exception('content value must not be None')
    return markdown.markdown(content, extensions=['tables'])

def send_file_raw(path:str=None):
    path = os.path.join(CONTENT_DIR, path)
    return flask.send_file(path)


def generate_page(path:str=None):
    try:
        path = os.path.join(CONTENT_DIR, path)
        print(path)
        with open(path, 'r+') as file:
            blog_md = file.read()
            file.close()
        blog_md_html = markdown_to_html(blog_md)
        blog_template = get_template('file/view_blog.html')
        return blog_template.render(blog_html=blog_md_html)
    except FileNotFoundError:
        return generate_page('error/404.md')