class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        # head.next will be least recently used
        # tail.prev will be most recetnlty ysed
        # head and tail will be placeholders at start and end respectively

        self.cache = {}
        self.cap = capacity
        self.head = Node(0, 0)
        self.tail = Node(0 ,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: Node) -> None:
        # always remove the head.next node
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def insert(self, node: Node) -> None:
        # always insert before self.tail
        prev = self.tail.prev
        next = self.tail
        prev.next = next.prev = node
        node.next = next
        node.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
        
