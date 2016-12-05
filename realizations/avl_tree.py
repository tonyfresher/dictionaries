from realizations.tree import TreeDict


class AVLTreeDict(TreeDict):
    '''Dictionary on a AVL-tree'''
    def _insert(self, root, key, value):
        if not self._root:
            self._root = TreeNode(key, value)

        elif root.key == key:
            root.value = value

        elif key < root.key:
            if root.left:
                self._insert(root.left, key, value)
            else:
                root.left = TreeNode(key, value, parent=root)
                self._update_balance(root.left)
        else:
            if root.right:
                self._insert(root.right, key, value)
            else:
                root.right = TreeNode(key, value, parent=root)
                self._update_balance(root.right)

    def _remove(self, root, key):
        if not root:
            raise KeyError(key)

        if key < root.key:
            self._remove(root.left, key)

        elif key > root.key:
            self._remove(root.right, key)

        elif key == root.key:
            p = root.parent

            if not root.left and not root.right:
                if root is self._root:
                    self._root = None

                elif root is p.left:
                    p.left = None
                else:
                    p.right = None

            elif not root.left or not root.right:
                if root is self._root:
                    self._root = root.left or root.right

                if not root.left:
                    if p:
                        if root is p.left:
                            p.left = root.right
                        else:
                            p.right = root.right
                    root.right.parent = p
                else:
                    if p:
                        if root is p.left:
                            p.left = root.left
                        else:
                            p.right = root.left
                    root.left.parent = p

            elif root.left and root.right:
                left_leaf = root.right
                while left_leaf.left:
                    left_leaf = left_leaf.left

                root.key = left_leaf.key
                root.value = left_leaf.value
                self._remove(left_leaf, left_leaf.key)

    def _update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self._rebalance(node)

        elif node.parent:
            if node is node.parent.left:
                node.parent.balance_factor += 1
            elif node is node.parent.right:
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self._update_balance(node.parent)

    def _rebalance(self, node):
        if node.balance_factor < 0:
            if node.right.balance_factor > 0:
                self._rotate_right(node.right)

            self._rotate_left(node)

        elif node.balance_factor > 0:
            if node.left.balance_factor < 0:
                self._rotate_left(node.left)

            self._rotate_right(node)

    def _rotate_left(self, root):
        new_root = root.right
        root.right = new_root.left

        if new_root.left:
            new_root.left.parent = root

        new_root.parent = root.parent

        if not root.parent:
            self._root = new_root
        else:
            if root is root.parent.left:
                root.parent.left = new_root
            else:
                root.parent.right = new_root

        new_root.left = root
        root.parent = new_root

        root.balance_factor = (root.balance_factor + 1 -
                               min(new_root.balance_factor, 0))
        new_root.balance_factor = (new_root.balance_factor + 1 +
                                   max(root.balance_factor, 0))

    def _rotate_right(self, root):
        new_root = root.left
        root.left = new_root.right

        if new_root.right:
            new_root.right.parent = root

        new_root.parent = root.parent

        if not root.parent:
            self._root = new_root
        else:
            if root is root.parent.left:
                root.parent.left = new_root
            else:
                root.parent.right = new_root

        new_root.right = root
        root.parent = new_root

        root.balance_factor = (root.balance_factor - 1 -
                               max(new_root.balance_factor, 0))
        new_root.balance_factor = (new_root.balance_factor + 1 +
                                   max(root.balance_factor, 0))


class TreeNode():
    '''Represents a AVL-tree node'''
    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value

        self.parent = parent
        self.left = None
        self.right = None

        self.balance_factor = 0

    def __eq__(self, other):
        return self.key == other.key

    def __str__(self):
        return '{}: {}'.format(self.key, self.value)
