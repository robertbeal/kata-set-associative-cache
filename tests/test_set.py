from cache.set import Set
import unittest
import uuid

class TestSet(unittest.TestCase):

    def test_it_returns_none_for_cache_misses(self):
        set = Set(1,TestPolicy())
        self.assertEqual(set.get(uuid.uuid4()), None)

    def test_it_returns_an_item_for_a_cache_hit(self):
        item = Item(uuid.uuid4(), uuid.uuid4(), timedelta(days=1))

        set = Set(1, TestPolicy())
        set.add(item)

        self.assertEqual(set.get(item.tag), item.data)

    def test_it_replaces_an_existing_item_when_adding(self):
        set = Set(1, TestPolicy())
        set.add(TestItem('foo', 123))
        set.add(TestItem('foo', 456))

        self.assertEqual(set.get('foo'), 456)

    def test_it_ejects_whatever_the_cache_policy_specifies(self):
        set = Set(1, TestPolicy())
        set.add(TestItem('foo', 123))
        set.add(TestItem('bar', 456))

        self.assertEqual(set.get('foo'), None)
        self.assertEqual(set.get('bar'), 456)

class TestPolicy:
    def remove(self, items):
        items.popitem()

from cache.item import Item
from datetime import timedelta

class TestItem(Item):
    def __init__(self, tag, data):
        Item.__init__(self, tag, data, timedelta(days=1))
