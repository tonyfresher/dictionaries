from collections import MutableMapping


class TreeDict(MutableMapping):
    '''Dictionary on a binary search tree'''
    def __init__(self, **kwargs):
        self._count = 0
        self._root = None

        for key, value in kwargs.items():
            self._insert(self.root, key, value)
            self._count += 1

    @property
    def root(self):
        return self._root

    def __setitem__(self, key, value):
        search_result = self._find(self.root, key)

        if not search_result:
            self._insert(self.root, key, value)
            self._count += 1
        else:
            search_result.value = value

    def __getitem__(self, key):
        search_result = self._find(self.root, key)

        if not search_result:
            raise KeyError(key)

        return search_result.value

    def __delitem__(self, key):
        self._remove(self.root, key)
        self._count -= 1

    def __contains__(self, key):
        return bool(self._find(self.root, key))

    def __iter__(self):
        yield from self._traverse(self.root)

    def __len__(self):
        return self._count

    def __str__(self):
        return str(dict(self))

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
        else:
            if root.right:
                self._insert(root.right, key, value)
            else:
                root.right = TreeNode(key, value, parent=root)

    def _find(self, root, key):
        if not root:
            return None

        if root.key == key:
            return root

        next_root = root.left if key < root.key else root.right

        if not next_root:
            return None
        return self._find(next_root, key)

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

    def _traverse(self, root):
        if not root:
            return

        yield from self._traverse(root.left)
        yield root.key
        yield from self._traverse(root.right)


class TreeNode():
    '''Represents a binary-search tree node'''
    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value

        self.parent = parent
        self.left = None
        self.right = None

    def __eq__(self, other):
        return self.key == other.key

    def __str__(self):
        return '{}: {}'.format(self.key, self.value)
