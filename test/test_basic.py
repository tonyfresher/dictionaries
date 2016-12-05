'''Basic tests for all dictionariess'''
import unittest
import abc

from realizations.linear_search import LinearSearchDict
from realizations.binary_search import BinarySearchDict
from realizations.tree import TreeDict
from realizations.avl_tree import AVLTreeDict
from realizations.hash_table import HashTableDict


class TestDictionary():
    '''Template class with basic tests for all realizations'''
    SOURCE = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

    def test_set_key(self):
        for key in self.dict:
            self.assertEqual(TestDictionary.SOURCE[key], self.dict[key])

        self.dict['a'] = 'another_one'
        self.assertEqual('another_one', self.dict['a'])


    def test_del_key(self):
        for key in TestDictionary.SOURCE:
            del self.dict[key]

        for key in TestDictionary.SOURCE:
            with self.assertRaises(KeyError):
                self.dict[key]

    def test_contains(self):
        for key in TestDictionary.SOURCE:
            self.assertTrue(key in self.dict)

    def test_wrong_key(self):
        with self.assertRaises(KeyError):
            self.dict['wrong']


class TestLinearDictionary(unittest.TestCase, TestDictionary):
    def setUp(self):
        self.dict = LinearSearchDict(**TestDictionary.SOURCE)


class TestBinaryDictionary(unittest.TestCase, TestDictionary):
    def setUp(self):
        self.dict = BinarySearchDict(**TestDictionary.SOURCE)


class TestTreeDictionary(unittest.TestCase, TestDictionary):
    def setUp(self):
        self.dict = TreeDict(**TestDictionary.SOURCE)

class TestAVLTreeDictionary(unittest.TestCase, TestDictionary):
    def setUp(self):
        self.dict = AVLTreeDict(**TestDictionary.SOURCE)


class TestHashTableDictionary(unittest.TestCase, TestDictionary):
    def setUp(self):
        self.dict = HashTableDict(**TestDictionary.SOURCE)


if __name__ == '__main__':
    unittest.main()
