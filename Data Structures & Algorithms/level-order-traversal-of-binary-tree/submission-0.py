# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ## Iterative BFS
        # queue = deque()
        # queue.append(root)
        # res = []
        # while len(queue) > 0:
        #     qLen = len(queue)
        #     level = []
        #     for i in range(qLen):
        #         curr = queue.popleft()
        #         if curr:
        #             level.append(curr.val)
        #             queue.append(curr.left)
        #             queue.append(curr.right)
        #     if level:
        #         res.append(level)

        # return res

        # Recursion
        res = []

        def dfs(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append([])
            
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 0)
        return res