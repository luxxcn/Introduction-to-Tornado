"""
Example 1-2. Handing input: string_service.py
测试，命令行运行：
curl http://localhost:8000/reverse/stressed
curl http://localhost:8000/wrap -d text=Lorem+ipsum+dolor+sit+amet,+consectetuer+adipiscing+elit.
"""
import textwrap
import signal
import logging
import time

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
# 调试模式，可ctrl+c结束进程，有改动自动重启
define('debug', default=True, type=bool, help='Run in debug mode')
define("port", default=8000, help="run on the given port", type=int)

class ReverseHandler(tornado.web.RequestHandler):
    def get(self, input):
        self.write(input[::-1])

class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument('text')
        width = self.get_argument('width', 40)

        self.write(textwrap.fill(text, width))

def shutdown(server):
    ioloop = tornado.ioloop.IOLoop.instance()
    logging.info('Stopping server.')
    server.stop()

    def finalize():
        ioloop.stop()
        logging.info('Stopped.')

    ioloop.add_timeout(time.time() + 1.5, finalize)

if __name__ == "__main__":
    
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r"/reverse/(\w+)", ReverseHandler),
        (r"/wrap", WrapHandler)
    ],debug=options.debug)
    http_server = tornado.httpserver.HTTPServer(app)

    http_server.listen(options.port)
    signal.signal(signal.SIGINT, lambda sig, frame: shutdown(http_server))
    logging.info('Starting server on localhost:{}'.format(options.port))

    tornado.ioloop.IOLoop.instance().start()