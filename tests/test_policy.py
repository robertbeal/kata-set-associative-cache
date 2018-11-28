import unittest
from collections import OrderedDict
from cache.policy import MRUPolicy, LRUPolicy

class TestMRUPolicy(unittest.TestCase):
    def test_it_returns_the_last_accessed_tag(self):
        policy = MRUPolicy()
        items = OrderedDict()
        items['foo'] = ''
        items['bar'] = ''
        items['bang'] = ''

        self.assertEqual(policy.remove(items)[0], 'bang')

class TestLRUPolicy(unittest.TestCase):
    def test_it_returns_the_least_accessed_tag(self):
        policy = LRUPolicy()
        items = OrderedDict()
        items['foo'] = ''
        items['bar'] = ''
        items['bang'] = ''

        self.assertEqual(policy.remove(items)[0], 'foo')
