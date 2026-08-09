class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.key_list = []

    def get(self, key: int) -> int:
        if key in self.cache:
            index = self.key_list.index(key)
            self.key_list.pop(index)
            self.key_list.insert(0, key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            index = self.key_list.index(key)
            self.key_list.pop(index)
            self.key_list.insert(0, key)
            self.cache[key] = value
        else:
            self.cache[key] = value
            self.key_list.insert(0, key)
            if len(self.cache) > self.capacity:
                least_key = self.key_list.pop()
                del self.cache[least_key]
