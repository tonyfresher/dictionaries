from collections import MutableMapping


class LinearSearchDict(MutableMapping):
    '''Dictionary on arrays with linear search'''
    def __init__(self, **kwargs):
        self._count = 0
        self._keys = list(kwargs.keys())
        self._values = list(kwargs.values())

    def __setitem__(self, key, value):
        if key not in self._keys:
            self._keys.append(key)
            self._values.append(value)
            self._count += 1
        else:
            self._values[self._keys.index(key)] = value

    def __getitem__(self, key):
        if key not in self._keys:
            raise KeyError(key)

        return self._values[self._keys.index(key)]

    def __delitem__(self, key):
        if key not in self._keys:
            raise KeyError(key)

        i = self._keys.index(key)
        self._values.pop(i)
        self._keys.pop(i)

    def __contains__(self, key):
        return key in self._keys

    def __iter__(self):
        for key in self._keys:
            yield key

    def __len__(self):
        return self._count

    def __str__(self):
        return str(dict(self))
