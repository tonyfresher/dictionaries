import math
from collections import MutableMapping


class HashTableDict(MutableMapping):
    '''Dictionary on a hash table'''
    START_SIZE = 128

    def __init__(self, **kwargs):
        self.pows = generate_pow(max(self.START_SIZE, len(kwargs)))

        self._build_table(kwargs)

    def __getitem__(self, key):
        entry = TableEntry(key, None)

        for bucket_entry in self._table[entry.hash % self._size]:
            if bucket_entry == entry:
                return bucket_entry.value

        raise KeyError(key)

    def __setitem__(self, key, value):
        if self._count + 1 == self._size:
            self._build_table(self)

        entry = TableEntry(key, value)

        for bucket_entry in self._table[entry.hash % self._size]:
            if bucket_entry == entry:
                bucket_entry.value = entry.value
                return

        self._table[entry.hash % self._size].append(entry)

    def __delitem__(self, key):
        entry = TableEntry(key, None)

        for bucket_entry in self._table[entry.hash % self._size]:
            if bucket_entry == entry:
                self._table[entry.hash % self._size].remove(bucket_entry)
                return

        raise KeyError(key)

    def __contains__(self, key):
        entry = TableEntry(key, None)
        for bucket_entry in self._table[entry.hash % self._size]:
            if bucket_entry == entry:
                return True

        return False

    def __iter__(self):
        for h in range(0, self._size):
            for entry in self._table[h]:
                yield entry.key

    def __len__(self):
        return self._count

    def __str__(self):
        return str(dict(self))

    def _build_table(self, source):
        size = next(self.pows)
        table = [[] for _ in range(size)]

        self._count = 0

        # fill the buckets
        for key, value in source.items():
            entry = TableEntry(key, value)
            table[entry.hash % size].append(TableEntry(key, value))

            self._count += 1

        self._table = table
        self._size = size


class TableEntry():
    '''Represents a hash table entry'''
    def __init__(self, key, value):
        self._key = key
        self._hash = hash(key)
        self.value = value

    @property
    def key(self):
        return self._key

    @property
    def hash(self):
        return self._hash

    def __eq__(self, other):
        return self._key == other.key


def generate_pow(start):
    '''Generates next power of 2'''
    power = 2**math.ceil(math.log2(start))
    while True:
        yield power
        power *= 2
