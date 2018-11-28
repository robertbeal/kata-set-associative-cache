import random

class Hasher:
    def hash(self, value):
        if type(value) == dict or type(value) == list:
            representation = frozenset(value)            
        else:
            representation = value

        return hash(representation)

class SetNumber:
    def __init__(self, size, hasher=Hasher()):
        self.__size = size
        self.__hasher = hasher
    
    def get(self, tag):
        random.seed(self.__hasher.hash(tag))
        return random.randint(0, (self.__size - 1))