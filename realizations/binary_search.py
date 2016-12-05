import bisect
from collections import MutableMapping


class BinarySearchDict(MutableMapping):
    '''Dictionary on sorted arrays with binary search'''
    def __init__(self, **kwargs):
        self._count = 0
        self._keys = sorted(list(kwargs.keys()))
        self._values = [kwargs[key] for key in self._keys]

    def __setitem__(self, key, value):
        if key not in self._keys:
            self._keys.append(key)
            self._keys.sort()
            self._values.insert(self._keys.index(key), value)
            self._count += 1
        else:
            i = bisect.bisect_left(self._keys, key)
            self._values[i] = value

    def __getitem__(self, key):
        i = bisect.bisect_left(self._keys, key)
        if i >= len(self._keys):
            raise KeyError(key)
        return self._values[i]

    def __delitem__(self, key):
        i = bisect.bisect_left(self._keys, key)
        if i >= len(self._keys):
            raise KeyError(key)
        self._values.pop(i)
        self._keys.pop(i)

    def __contains__(self, key):
        i = bisect.bisect_left(self._keys, key)
        return i < len(self._keys) and self._keys[i] == key

    def __iter__(self):
        for key in self._keys:
            yield key

    def __len__(self):
        return self._count

    def __str__(self):
        return str(dict(self))
