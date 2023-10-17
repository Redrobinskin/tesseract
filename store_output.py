```python
import pymongo

def init_db():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]
    return db

def store_output(json_output):
    db = init_db()
    collection = db["mycollection"]
    id = collection.insert_one(json_output).inserted_id
    return id
```