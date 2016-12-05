import unittest
from realizations.hash_table import HashTableDict


class TestHashTableDict(unittest.TestCase):
    def setUp(self):
        self.dict = HashTableDict()

    def test_overflow(self):
        for i in range(2 * HashTableDict.START_SIZE + 1):
            self.dict[i] = ''
