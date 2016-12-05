'''Tests TreeDict and AVLTreeDict'''
import unittest

from realizations.tree import TreeDict
from realizations.avl_tree import AVLTreeDict

class TestTree():
    def tearDown(self):
        self.assertTrue(is_bst(self.dict.root, float('-inf'), float('inf')))

    def test_del_root(self):
        self._insert_and_delete([0],
                                [0])

    def test_left_branch(self):
        self._insert_and_delete([0, -1, -2, -3],
                                [0, -3, -2, -1])

    def test_right_branch(self):
        self._insert_and_delete([0, 1, 2, 3],
                                [0, 3, 2, 1])

    def test_ideally_balanced(self):
        self._insert_and_delete([1, 3, 2, -4, -2, -8, 10],
                                [1, -2, 2, 3, -8, -4, 10])

    def test_unbalanced_left(self):
        self._insert_and_delete([1, 3, 2, -4, -2, -8, 10, -15, -17],
                                [1, -2, 2, 3, -8, -4, 10, -15, -17])

    def test_unbalanced_right(self):
        self._insert_and_delete([1, 3, 2, -4, -2, -8, 10, 15, 17],
                                [1, -2, 2, 3, -8, -4, 10, 15, 17])

    def test_cycle(self):
        self._insert_and_delete([1, 3, 2],
                                [1, 3, 2])

    def _insert_and_delete(self, insert, delete):
        '''Template test method'''
        for i in insert:
            self.dict[i] = i

        self.assertEqual(len(insert), len([x for x in self.dict]))

        for i in delete:
            del self.dict[i]

        self.assertEqual(len(insert) - len(delete), len([x for x in self.dict]))


class TestTreeDict(unittest.TestCase, TestTree):
    def setUp(self):
        self.dict = TreeDict()

class TestAVLTreeDict(unittest.TestCase, TestTree):
    def setUp(self):
        self.dict = AVLTreeDict()

def is_bst(root, min_val, max_val):
    '''Defines whether tree is binary-search or not'''
    if not root:
        return True

    return (root.key > min_val and root.key < max_val
            and is_bst(root.left, min_val, root.key)
            and is_bst(root.right, root.key, max_val))
