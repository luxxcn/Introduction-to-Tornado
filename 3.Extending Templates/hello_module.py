"""
Example 3-1.Module basics: hello_module.py
"""
import signal
import logging
import time

from os import path
import random

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, UIModule

from tornado.options import define, options, parse_command_line
# 调试模式，可ctrl+c结束进程，有改动自动重启
define('debug', default=True, type=bool, help='Run in debug mode')
define("port", default=8000, help="run on the given port", type=int)

class HelloHandler(RequestHandler):
    def get(self):
        self.render('hello.html')

class HelloModule(UIModule):
    def render(self):
        return '<h1>Hello, world!</h1>'

def shutdown(server):
    ioloop = IOLoop.instance()
    logging.info('Stopping server.')
    server.stop()

    def finalize():
        ioloop.stop()
        logging.info('Stopped.')

    ioloop.add_timeout(time.time() + 1.5, finalize)
    
if __name__ == "__main__":
    
    parse_command_line()

    handlers = [
        (r'/', HelloHandler),
    ]
    settings=dict(
        template_path=path.join(path.dirname(__file__), 'templates'),
        ui_modules={'Hello': HelloModule},
        debug=options.debug
    )
    app = Application(handlers, **settings)
    http_server = HTTPServer(app)

    http_server.listen(options.port)

    signal.signal(signal.SIGINT, lambda sig, frame: shutdown(http_server))
    logging.info('Starting server on localhost:{}'.format(options.port))

    IOLoop.instance().start()