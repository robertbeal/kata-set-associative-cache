from collections import OrderedDict

class MRUPolicy:   
    def remove(self, items):
        return items.popitem(last=True)

class LRUPolicy:   
    def remove(self, items):
        return items.popitem(last=False)