"""
Example 2-1. Simple forms and templates: poemmaker.py
测试：
1.运行：
python poemmaker.py --port=8000
2.浏览器中访问：
http://localhost:8000/
"""
import signal
import logging
import time

from os import path

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application

from tornado.options import define, options, parse_command_line
# 调试模式，可ctrl+c结束进程，有改动自动重启
define('debug', default=True, type=bool, help='Run in debug mode')
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(RequestHandler):
    def get(self):
        self.render('index.html')
        
class PoemPageHandler(RequestHandler):
    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render('poem.html', roads=noun1, wood=noun2, made=verb, difference=noun3)

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
        (r'/', IndexHandler),
        (r'/poem', PoemPageHandler)],
        template_path=path.join(path.dirname(__file__), "templates"),
        debug=options.debug)
    http_server = HTTPServer(app)

    http_server.listen(options.port)

    signal.signal(signal.SIGINT, lambda sig, frame: shutdown(http_server))
    logging.info('Starting server on localhost:{}'.format(options.port))

    IOLoop.instance().start()