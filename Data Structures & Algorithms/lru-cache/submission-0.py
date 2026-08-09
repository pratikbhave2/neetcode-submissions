class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.prev_node = None # Pointer to previous node
        self.next_node = None # Pointer to Next node

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = defaultdict(int)
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next_node = self.tail # head -> tail
        self.tail.prev_node = self.head # head <- tail
    
    def add_node(self, node: Node) -> None:
        # Add node after the head
        # E.g. Before adding: head <-> A <-> B <-> tail
        # After adding: head <-> node <-> A <-> B <-> tail
        # We add it after the head because that is the most recently used position
        node.next_node = self.head.next_node
        node.prev_node = self.head
        self.head.next_node.prev_node = node
        self.head.next_node = node

    def remove_node(self, node: Node) -> None:
        # Remove given node from the Double LL
        # E.g. Before removing: head <-> A <-> node <-> B <-> tail
        # After removing: head <-> A <-> B <-> tail
        prev_node = node.prev_node
        next_node = node.next_node
        prev_node.next_node = next_node
        next_node.prev_node = prev_node

    def get(self, key: int) -> int:
        # If key exists in self.cache, 
        # remove the node that corresponds to the key,
        # re-add the node in the LL(so that now it is the most recently used node)
        # Return the node.val
        # IF key does not exist in self.cache then return -1, no need to do anything in the LL
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            self.add_node(node)
            return node.val
        
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        # If key exists in self.cache, remove the node that corresponds to it from the LL
        # create new node with key & value, and add it to the LL (so that it is the most recent used)
        # Also add/update the key in self.cache with this new node
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
        
        new_node = Node(key, value)
        self.add_node(new_node)
        self.cache[key] = new_node

        # Also check if we have exceeded the capacity by checking len(self.cache)
        if len(self.cache) > self.capacity:
            # Now we need to remove the Least recently used node
            # which will be tail.prev
            # Remove it from the LL 
            # Also remove it from self.cache by calling least.key
            least = self.tail.prev_node
            self.remove_node(least)
            del self.cache[least.key]
