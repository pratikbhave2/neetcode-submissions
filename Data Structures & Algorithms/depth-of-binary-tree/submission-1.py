# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative DFS
        # height = 0
        # if root is None:
        #     return height

        # stack = [(root, 1)]

        # while len(stack) > 0:
        #     curr, curr_height = stack.pop()
            
        #     if curr is not None:
        #         height = max(height, curr_height)
        #         stack.append((curr.left, curr_height + 1))
        #         stack.append((curr.right, curr_height + 1))
        # return height

        # Recursion

        if not root:
            return 0
        
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        return max(left_height, right_height) + 1