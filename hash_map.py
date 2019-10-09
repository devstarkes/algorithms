class MyHashMap:

    def __init__(self):
        self.num_buckets = 100
        self.buckets = [-1] * self.num_buckets

    def _hash(self, key):
        return key % self.num_buckets

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)

        if self.buckets[index] == -1:
            self.buckets[index] = []

        for i, kv_pair in enumerate(self.buckets[index]):
            if kv_pair[0] == key:
                self.buckets[index][i] = (key, value)
                return

        self.buckets[index].append((key, value))

    def get(self, key: int) -> int:
        index = self._hash(key)

        if self.buckets[index] == -1:
            return -1

        for kv_pair in self.buckets[index]:
            if kv_pair[0] == key:
                return kv_pair[1]

        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)

        index_to_remove = -1

        if self.buckets[index] == -1:
            return

        for i, kv_pair in enumerate(self.buckets[index]):
            if kv_pair[0] == key:
                index_to_remove = i
                break

        if index_to_remove == -1:
            return
        else:
            del self.buckets[index][index_to_remove]
