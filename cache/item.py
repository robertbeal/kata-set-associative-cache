from datetime import datetime

class Item:
    def __init__(self, tag, data, ttl):
        self.tag = tag
        self.data = data
        self.expires = datetime.utcnow()+ ttl