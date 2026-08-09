class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(0, 0) # self.head.next will contain LRU
        self.tail = Node(0, 0) # self.tail.prev will contain MRU
        self.head.next = self.tail
        self.tail.prev = self.head


    def add_node(self, node: Node) -> None:
        # Always add to the end beetween self.tail.prev and self.tail so that it will correspond to Most recently Used
        prev = self.tail.prev
        next = self.tail
        prev.next = next.prev = node
        node.prev = prev
        node.next = next

    def remove_node(self, node: Node) -> None:
        # Always remove Self.head.next which will be the Least recently used
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            self.add_node(node)
            return node.val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key]) # Remove so that we can re-put it with updated value
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.add_node(new_node)

        # check length
        if len(self.cache) > self.capacity:
            lru_node = self.head.next
            self.remove_node(lru_node)
            del self.cache[lru_node.key]

