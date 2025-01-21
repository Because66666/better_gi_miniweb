from gevent import pywsgi
from main import app
server = pywsgi.WSGIServer(('0.0.0.0', 222), app)
print('Running...')
server.serve_forever()
