import os
import flask
from .util import generate_page


    
def get_file(filename):
    # return 404 if file doesn't exist
    if f'{filename}' not in os.listdir('file/') : return generate_page('error/404.md'), 404
    return flask.send_file(f'file/{filename}')


def start(host:str='0.0.0.0', port:int=8080, debug:bool=False) -> flask.Flask:
    app = flask.Flask('markdown-server')
    app.url_map.strict_slashes = False

    @app.route('/<branch>/<name>/', methods=['GET'])
    def blog_view(branch, name):
        if branch.lower() == 'file' : return get_file(name), 200
        
        if f'{name}.md' not in os.listdir(f'{branch}/') : return generate_page('error/404.md'), 404
        
        return generate_page(f'{branch}/{name}.md'), 200



    app.run(host, port, debug)