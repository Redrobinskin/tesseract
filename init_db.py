```python
from pymongo import MongoClient

def init_db():
    """
    Initialize a NoSQL database. If the database doesn't exist, create it.
    """
    client = MongoClient('localhost', 27017)
    db = client['image_text_db']
    return db
```