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
import random

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application

from tornado.options import define, options, parse_command_line
# 调试模式，可ctrl+c结束进程，有改动自动重启
define('debug', default=True, type=bool, help='Run in debug mode')
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(RequestHandler):
    def get(self):
        # self.render('index.html')
        self.render('index24.html')
        
class MungedPageHandler(RequestHandler):
    def map_by_first_letter(self, text):
        mapped = dict()
        for line in text.split('\r\n'):
            for word in [x for x in line.split(' ') if len(x) > 0]:
                if word[0] not in mapped:
                    mapped[word[0]] = []
                mapped[word[0]].append(word)

        return mapped

    def post(self):
        source_text = self.get_argument('source')
        text_to_change = self.get_argument('change')
        source_map = self.map_by_first_letter(source_text)
        change_lines = text_to_change.split('\r\n')
        self.render('munged.html', source_map=source_map, 
            change_lines=change_lines, choice=random.choice)

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
        (r'/poem', MungedPageHandler)],
        template_path=path.join(path.dirname(__file__), "templates"),
        static_path=path.join(path.dirname(__file__), "static"),
        debug=options.debug)
    http_server = HTTPServer(app)

    http_server.listen(options.port)

    signal.signal(signal.SIGINT, lambda sig, frame: shutdown(http_server))
    logging.info('Starting server on localhost:{}'.format(options.port))

    IOLoop.instance().start()