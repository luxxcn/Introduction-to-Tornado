"""
Burt's Book 初始化数据库数据
"""

import pymongo

def initBurtsBooksDB():
    conn = pymongo.MongoClient('localhost', 27017)
    db = conn['bookstore']
    db.books.insert_one({
        "title": "Programming Collective Intelligence",
        "subtitle": "Building Smart Web 2.0 Applications",
        "image": "/static/images/collective_intelligence.gif",
        "author": "Toby Segaran",
        "date_added": 1310248056,
        "date_released": "August 2007",
        "isbn": "978-0-596-52932-1",
        "description": "<p>[...]</p>"
    })
    db.books.insert_one({
        "title": "RESTful Web Services",
        "subtitle": "Web services for the real world",
        "image": "/static/images/restful_web_services.gif",
        "author": "Leonard Richardson, Sam Ruby",
        "date_added": 1311148056,
        "date_released": "May 2007",
        "isbn": "978-0-596-52926-0",
        "description": "<p>[...]</p>"
    })

if __name__ == "__main__":
    initBurtsBooksDB()