from pymongo import MongoClient

def load_to_mongodb(data, collection_name):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['marinhoia']
    collection = db[user]
    collection.insert_many(data)
