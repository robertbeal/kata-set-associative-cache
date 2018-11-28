import unittest
import uuid
from cache.setAssociativeCache import Cache
from cache.policy import MRUPolicy

class TestCache(unittest.TestCase):
    def test_it_returns_an_item(self):
        tag = uuid.uuid4()
        data = uuid.uuid4()

        cache = Cache(uuid.UUID, uuid.UUID, 5, 10, MRUPolicy())
        cache.add(tag, data)

        self.assertEqual(cache.get(tag), data)

    def test_it_returns_none(self):
        cache = Cache(uuid.UUID, uuid.UUID, 5, 10, MRUPolicy())

        self.assertEqual(cache.get(uuid.uuid4()), None)

    def test_building_a_cache(self):
        tag = uuid.uuid4()
        data = uuid.uuid4()
        
        cache = Cache(uuid.UUID, uuid.UUID, 5, 10, MRUPolicy())
        self.assertEqual(cache.get(uuid.uuid4()), None)

        cache.add(tag, data)
        self.assertEqual(cache.get(tag), data)

    def test_tag_is_type_safe_when_getting(self):
        cache = Cache(int, str, 5, 10, MRUPolicy())
        cache.get(123)
        return self.assertRaises(ValueError, cache.get, 'foo')

    def test_tag_is_type_safe_when_adding(self):
        cache = Cache(int, str, 5, 10, MRUPolicy())
        cache.add(123, '')
        return self.assertRaises(ValueError, cache.add, 'foo', '')

    def test_value_is_type_safe_when_adding(self):
        cache = Cache(str, int, 5, 10, MRUPolicy())
        cache.add('123', 123)
        return self.assertRaises(ValueError, cache.add, '123', '')