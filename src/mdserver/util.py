import jinja2
import markdown


def get_template(path:str=None) -> jinja2.Template:
    if path == None : raise Exception('path value must not be None')
    with open(path, "r+") as file:
        content = file.read()
        file.close()
    return jinja2.Template(content)

def markdown_to_html(content:str=None):
    if content == None : raise Exception('content value must not be None')
    return markdown.markdown(content, extensions=['tables'])

blog_template = get_template('file/view_blog.html')


def generate_page(md_path:str=None):
    with open(md_path, 'r+') as file:
        blog_md = file.read()
        file.close()

        blog_md_html = markdown_to_html(blog_md)
        blog_template = get_template('file/view_blog.html')

        return blog_template.render(blog_html=blog_md_html)