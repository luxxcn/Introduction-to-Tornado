"""
Example 1-1. The basics: hello.py
运行：python hello.py --port=8000
浏览器访问：http://localhost:8000/
命令行访问：curl http://localhost:8000/?greeding=Salutations
"""

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', firendly user!')

if __name__ == "__main__":
    
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)

    http_server.listen(options.port)

    tornado.ioloop.IOLoop.instance().start()