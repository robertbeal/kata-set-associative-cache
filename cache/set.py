from collections import OrderedDict
from threading import Lock

class Set:
    def __init__(self, size, policy):
        self.items = dict()
        self.size = size
        self.policy = policy
        self.__lock = Lock()

    def get(self, tag):
        with self.__lock:
            try:
                item = self.items.pop(tag)
                self.items[tag] = item
                return item.data
            except KeyError:
                return None

    def add(self, item):
        with self.__lock:
            try:
                if len(self.items) >= self.size:
                    self.policy.remove(self.items)
            finally:
                self.items[item.tag] = item