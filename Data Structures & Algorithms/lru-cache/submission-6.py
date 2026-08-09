class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.key_list = [] #Stores the keys used in self.cache
        # IDea is to put most recently used in front of the list
        # and least recently used in the back
        # That we we can just pop from the end
        # We will also have to change the order of keys based on the call that is receievd to get


    def get(self, key: int) -> int:
        if key in self.cache:
            # Shift this key to the front in self.key_list
            index = self.key_list.index(key)
            self.key_list.pop(index)
            self.key_list.insert(0, key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # always insert in the front
        if key in self.cache:
            index = self.key_list.index(key)
            self.key_list.pop(index)
            self.key_list.insert(0, key)

        else: # Add the key to cache and also to self.key_list
             # Update the value
            self.key_list.insert(0, key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            least_key = self.key_list.pop()
            del self.cache[least_key]


