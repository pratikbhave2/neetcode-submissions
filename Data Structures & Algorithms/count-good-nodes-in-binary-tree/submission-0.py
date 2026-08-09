# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [(root, -float('inf'))]
        count = 0 # Root node
        while len(stack) > 0:
            curr, max_val = stack.pop()
            if curr.val >= max_val:
                count += 1

            if curr.left is not None:
                stack.append((curr.left, max(max_val, curr.val)))
            if curr.right is not None:
                stack.append((curr.right, max(max_val, curr.val)))            

        return count
