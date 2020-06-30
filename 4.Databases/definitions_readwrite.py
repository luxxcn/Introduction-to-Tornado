"""
Example 4-2.A read/write dictionary service: definitions_readwrite.py
"""
import signal
import logging
import time

from os import path
import random

import pymongo

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado import web
from tornado.web import RequestHandler

from tornado.options import define, options, parse_command_line
# 调试模式，可ctrl+c结束进程，有改动自动重启
define('debug', default=True, type=bool, help='Run in debug mode')
define("port", default=8000, help="run on the given port", type=int)

class Application(web.Application):
    def __init__(self):
        handlers = [
            (r'/(\w+)', WordHandler)
        ]
        settings = dict(
            debug=options.debug
        )
        # pymongo.Connection 已被弃用
        conn = pymongo.MongoClient('localhost', 27017)
        self.db = conn['definitions']
        web.Application.__init__(self, handlers, **settings)

class WordHandler(RequestHandler):
    def get(self, word):
        coll = self.application.db.words
        word_doc = coll.find_one({"word": word})
        if word_doc:
            del word_doc["_id"]
            self.write(word_doc)
        else:
            self.set_status(404)
            self.write({"error": "word not found"})

    def post(self, word):
        definition = self.get_argument('definition')
        coll = self.application.db.words
        word_doc = coll.find_one({"word": word})
        if word_doc:
            word_doc['definition'] = definition
            coll.save(word_doc)
        else:
            word_doc = {'word': word, 'definition': definition}
            coll.insert_one(word_doc)
        del word_doc["_id"]
        self.write(word_doc)

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
    app = Application()
    http_server = HTTPServer(app)

    http_server.listen(options.port)

    signal.signal(signal.SIGINT, lambda sig, frame: shutdown(http_server))
    logging.info('Starting server on localhost:{}'.format(options.port))

    IOLoop.instance().start()