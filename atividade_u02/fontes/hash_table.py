class HashTable:
    def __init__(self):
        self.size = 1
        self.table = [[]]

    def _hash_function(self, key):
        return key % self.size

    def _re_hash(self):
        self.size = self.size * 2
        old_table = self.table
        self.table = [[] for _ in range(self.size)]
        for item in old_table:
            if item:
                if len(item) > 1:
                    for i in item:
                        self.insert(i)
                else:
                    self.insert(item[0])

    def insert(self, value):
        if len(self.table[self._hash_function(value)]) >= self.size:
            self._re_hash()

        self.table[self._hash_function(value)].append(value)

    def search(self, value):
        index = self._hash_function(value)
        if self.table[index]:
            for item in self.table[index]:
                if item == value:
                    return True
        return False
