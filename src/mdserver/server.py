import os
import flask
from .util import make_default_dirs, send_file_raw, send_blog_page
import pathlib

from mdserver.models.page import BlogPage

path = os.environ.get('CONTENT_PATH', './content')
ROOT_CONTENT_PATH = pathlib.Path(path)
STATIC_CONTENT_FOLDER = ROOT_CONTENT_PATH / 'static'


def get_file(filename):
    # return 404 if file doesn't exist
    if f'{filename}' not in os.listdir(STATIC_CONTENT_FOLDER) : return send_blog_page('error/404.md'), 404
    return flask.send_file(f'static/{filename}')


def start(host:str='0.0.0.0', port:int=8081, debug:bool=False) -> flask.Flask:

    static_content_folder = ROOT_CONTENT_PATH / 'static'
    
    app = flask.Flask('markdown-server', static_folder=static_content_folder, template_folder=ROOT_CONTENT_PATH)
    app.url_map.strict_slashes = False

    # /favicon.ico
    @app.route('/favicon.ico', methods=['GET'])
    def favicon() : return BlogPage('error/404').render(), 404

    # /
    @app.route('/', methods=['GET'])
    def root() : return '/blog/', 304

    # # /blog/
    # @app.route('/blog/', methods=['GET'])
    # def blog_root() : return '/blog/example-md', 304

    @app.route('/<path:branch>/', methods=['GET'])
    def get_file(branch):
        #
        # endpoint for general fetching blogs and files
        # via /blog/ and /file/ respectively
        #
        split_branch = list(filter(None, branch.split('/')))
        domain = split_branch[0]
        match domain:
            case 'static':
                path = os.path.join(*split_branch)
                return send_file_raw(path)
            case 'blog':
                return BlogPage(path=branch).render()
            case _:
                return 'error', 404
        


    make_default_dirs()
    app.run(host, port, debug)