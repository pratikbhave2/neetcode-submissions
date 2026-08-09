# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative BFS
        # res = []
        # queue = collections.deque()
        # queue.append(root)
        # while queue:
        #     qLen = len(queue)
        #     level = []
        #     for i in range(qLen):
        #         curr = queue.popleft()
        #         if curr:
        #             level.append(curr.val)
        #             queue.append(curr.left)
        #             queue.append(curr.right)
        #     if level:
        #         res.append(level.pop())

        # return res

        # DFS recursive

        # res = []

        # def dfs(node, depth):
        #     if not node:
        #         return None
        #     if depth == len(res):
        #         res.append(node.val)
            
        #     dfs(node.right, depth + 1)
        #     dfs(node.left, depth + 1)
        
        # dfs(root, 0)
        # return res

        if not root:
            return []

        q = collections.deque()
        q.append([root, 1])
        level_list = []
        prev_level = 0
        while len(q) > 0:
            curr, level = q.popleft()

            if prev_level != level:
                level_list.append(curr.val)
                prev_level = level

            if curr.right:
                q.append((curr.right, level+ 1))

            if curr.left:
                q.append((curr.left, level + 1))

        return level_list