import os
import flask
from .util import get_template, markdown_to_html

def start(host:str='0.0.0.0', port:int=8080, debug:bool=False) -> flask.Flask:
    app = flask.Flask('markdown-server')
    app.url_map.strict_slashes = False

    @app.route('/blog/<name>/', methods=['GET'])
    def blog_view(name):
        # return if blog doesn't exist
        if f'{name}.md' not in os.listdir('blog/') : return "blog not found (404)", 404
        
        with open(f'blog/{name}.md', 'r+') as file:
            blog_md = file.read()
            file.close()

        blog_md_html = markdown_to_html(blog_md)
        blog_template = get_template('file/view_blog.html')

        return blog_template.render(blog_html=blog_md_html), 200
    
    @app.route('/file/<filename>/', methods=['GET'])
    def file_get(filename):
        # return 404 if file doesn't exist
        if f'{filename}' not in os.listdir('file/') : return "file not found (404)", 404
        
        return flask.send_file(f'file/{filename}')


    app.run(host, port, debug)