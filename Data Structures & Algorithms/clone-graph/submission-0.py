"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # DFS
        # O ( V + E)
        # old_to_new = {}
        # def dfs(node):
        #     if node in old_to_new:
        #         return old_to_new[node]

        #     copy = Node(node.val)
        #     old_to_new[node] = copy

        #     for neighbor in node.neighbors:
        #         copy.neighbors.append(dfs(neighbor))
        #     return copy

        # if node:
        #     return dfs(node)
        # return None

        # BFS
        # O ( V + E)
        if not node:
            return None
        old_to_new = {}
        queue = deque()
        old_to_new[node] = Node(node.val)
        queue.append(node)

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                old_to_new[curr].neighbors.append(old_to_new[neighbor])

        return old_to_new[node]


