import mdserver.server

# for key in os.environ:
#     print(f'{key}={os.environ[key]}')

# hey, here's another comment

server = mdserver.server.start(debug=True, port=8001)
