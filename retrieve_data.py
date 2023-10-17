```python
from pymongo import MongoClient

def retrieve_data(id=None):
    client = MongoClient('localhost', 27017)
    db = client['image_text_db']
    collection = db['image_texts']

    if id:
        data = collection.find_one({'_id': id})
    else:
        data = list(collection.find())

    return data
```