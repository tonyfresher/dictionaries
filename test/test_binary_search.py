import unittest
from realizations.binary_search import BinarySearchDict


class TestBinarySearchDict(unittest.TestCase):
    def setUp(self):
        self.dict = BinarySearchDict()

    def test_odd_equals(self):
        self._insert(1, 2, 2, 2, 2)
        self.assertEqual(True, 1 in self.dict)

    def test_even_equals(self):
        self._insert(1, 2, 2, 2, 2, 2)
        self.assertEqual(True, 1 in self.dict)

    def _insert(self, *args):
        for key in args:
            self.dict[key] = ''
