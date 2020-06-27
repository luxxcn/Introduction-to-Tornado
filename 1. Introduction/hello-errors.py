"""
Example 1-3. Custom error response: hello-errors.py
测试，命令行运行：
curl -d foo=bar http://localhost:8000/
"""
import signal
import logging
import time

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application

from tornado.options import define, options, parse_command_line
# 调试模式，可ctrl+c结束进程，有改动自动重启
define('debug', default=True, type=bool, help='Run in debug mode')
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', fridenly user!')

    def write_error(self, status_code, **kwargs):
        self.write('Gosh darnit, user! You caused a %d error.' % status_code)

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
    app = Application(handlers=[
        (r"/", IndexHandler)
    ],debug=options.debug)
    http_server = HTTPServer(app)

    http_server.listen(options.port)
    signal.signal(signal.SIGINT, lambda sig, frame: shutdown(http_server))
    logging.info('Starting server on localhost:{}'.format(options.port))

    IOLoop.instance().start()