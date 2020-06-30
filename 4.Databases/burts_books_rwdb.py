"""
Example 4-3.Reading from the database: burts_books_db.py
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
            (r'/', MainHandler),
            (r'/recommended', RecommendedHandler),
            (r'/edit/([0-9Xx\-]+)', BookEditHandler),
            (r'/add', BookEditHandler)
        ]
        settings = dict(
            template_path=path.join(path.dirname(__file__), "templates"),
            static_path=path.join(path.dirname(__file__), "static"),
            ui_modules={"Book": BookModule},
            debug=options.debug
        )
        # pymongo.Connection 已被弃用
        conn = pymongo.MongoClient('localhost', 27017)
        self.db = conn['bookstore']
        web.Application.__init__(self, handlers, **settings)

class MainHandler(RequestHandler):
    def get(self):
        self.render(
            "index.html", page_title="Burt's Books | Home",
            header_text="Welcome to Burt's Books!",
        )

class RecommendedHandler(RequestHandler):
    def get(self):
        coll = self.application.db.books
        books = coll.find()
        self.render(
            "recommended.html",
            page_title="Burt's Book | Recommended Reading",
            header_text = "Recommmended Reading",
            books = books
        )

class BookEditHandler(RequestHandler):
    def get(self, isbn=None):
        book = dict()
        if isbn:
            coll = self.application.db.books
            book = coll.find_one({'isbn': isbn})
            if book is None:
                book = dict()
        self.render(
            "book_edit.html",
            page_title="Burt's Books",
            header_text="Edit book",
            book=book
        )

    def post(self, isbn=None):
        book_fields = ['isbn', 'title', 'subtitle', 'image', 'author', 'date_released', 'description']
        coll = self.application.db.books
        book = dict()
        if isbn:
            book = coll.find_one({"isbn": isbn})
        for key in book_fields:
            book[key] = self.get_argument(key, None)
            
        if isbn:
            coll.save(book)
        else:
            book['date_added'] = int(time.time())
            coll.insert(book)
        self.redirect("/recommended")

class BookModule(web.UIModule):
    def render(self, book):
        return self.render_string(
            "modules/book.html",
            book=book,
        )
    def css_files(self):
        return "/static/css/recommended.css"
    def javascript_files(self):
        return "/staticjs/recommended.js"

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