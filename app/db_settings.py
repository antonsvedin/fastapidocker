from pymongo import MongoClient
from dotenv import load_dotenv
import os

def returnAllUsers():
    load_dotenv()
    client = MongoClient(os.getenv("mongodb_uri", os.getenv("port")))
    db = client.testdb
    collection = db.user
    return collection.find({})
