import os
import flask
from .util import generate_page, send_file_raw


def get_file(filename):
    # return 404 if file doesn't exist
    if f'{filename}' not in os.listdir('file/') : return generate_page('error/404.md'), 404
    return flask.send_file(f'file/{filename}')


def start(host:str='0.0.0.0', port:int=8080, debug:bool=False) -> flask.Flask:
    app = flask.Flask('markdown-server')
    app.url_map.strict_slashes = False

    # /
    @app.route('/', methods=['GET'])
    def root() : return '/blog/', 304

    # /blog/
    @app.route('/blog/', methods=['GET'])
    def blog_root() : return '/blog/example-md', 304

    @app.route('/<path:branch>/', methods=['GET'])
    def get_file(branch):
        #
        # 
        #
        split_branch = list(filter(None, branch.split('/')))
        domain = split_branch[0]
        print(f'domain="{domain}", split_branch={split_branch}')
        print(domain)
        if domain == 'file':
            path = os.path.join(*split_branch)
            print(path)
            return send_file_raw(path)
            
        if domain == 'blog':
            split_branch[-1] = split_branch[-1] + '.md'
            return generate_page(os.path.join(*split_branch)) 

    app.run(host, port, debug)