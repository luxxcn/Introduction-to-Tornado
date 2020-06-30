"""
definitions_readonly.py 用测试数据（mongoDB）
"""

import pymongo

def initWords():
    conn = pymongo.MongoClient('localhost', 27017)
    db = conn.example
    # insert已被弃用，需用insert_one或insert_many
    db.words.insert_one({
        "word": "oarlock", 
        "definition": "A device attached to a rowboat to hold the oras in place"
    })
    db.words.insert_one({
        "word": "seminomadic",
        "definition": "Only partially nomadic"
    })
    db.words.insert_one({
        "word": "perturb",
        "definition": "Bother, unsettle, modify"
    })

if __name__ == "__main__":
    initWords()