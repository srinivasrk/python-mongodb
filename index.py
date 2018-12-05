import pymongo
import os
import datetime
from threading import Timer


def update_post():
    post = {"author": "Mike",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}
    collection.update_one({'_id': post_id}, {"$set": post}, upsert=False)


client = pymongo.MongoClient("mongodb://" + os.environ['MONGOSERVER']+ ":27017/")
db = client.test_database
collection = db.test_collection
collection.delete_many({})  # remove all old data
post = {"author": "Mike",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}
post_id = collection.insert_one(post).inserted_id
print("Document created")

t = Timer(10.0, update_post)
t.start()  # after 30 seconds, "update the document"

