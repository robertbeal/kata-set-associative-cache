import unittest
import uuid
from cache.setNumber import SetNumber, Hasher

class TestSetNumber(unittest.TestCase):
    def test_it_returns_the_same_set_number(self):
        number = SetNumber(10, HasherStub())
        self.assertEqual(number.get(''), number.get(''))

class HasherStub:
    def hash(self, value):
        return 'some-random-hash-value'

class TestHasher(unittest.TestCase):
    def test_it_hashes_a_string(self):
        Hasher().hash('foo')

    def test_it_hashes_a_class(self):
        Hasher().hash(FooClass()) 

    def test_it_hashes_a_list(self):
        Hasher().hash([]) 

    def test_it_hashes_a_dict(self):
        Hasher().hash(dict()) 

class FooClass:
    def __init(self):
        self.name = 'test'