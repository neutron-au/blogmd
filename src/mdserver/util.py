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

# html_content = markdown_to_html(markdown_text)
# x = blog_template.render(blog_html=html_content)
# with open('a.html', 'w+') as file:
#     file.write(x)
#     file.close()