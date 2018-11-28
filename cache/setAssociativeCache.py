from datetime import timedelta
from cache.set import Set
from cache.setNumber import SetNumber
from cache.item import Item

class Cache:
    def __init__(self, T, V, sets, size, policy):
        self.__T = T
        self.__V = V
        self.__sets = [Set(size, policy) for _ in range(sets)]
        self.__number = SetNumber(sets)

    def get(self, tag):
        self.check_type(tag, self.__T)
        
        set = self.__number.get(tag)

        return self.__sets[set].get(tag)

    def add(self, tag, data, ttl=timedelta(hours=1)):
        self.check_type(tag, self.__T)
        self.check_type(data, self.__V)
        
        set = self.__number.get(tag)
        item = Item(tag, data, ttl)

        self.__sets[set].add(item)
    
    def check_type(self, instance, typeOf):
        if not isinstance(instance, typeOf):
            raise ValueError('{} is not a valid instance of {}'.format(type(instance), typeOf))