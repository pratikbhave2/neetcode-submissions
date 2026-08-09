# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Brute force
        # Handle null cases upfront
        if not p and not q:
            return True
        if not p or not q:
            return False

        # Brute force: Compare Pre-order traversal lists
        def traverse(root):
            if not root:
                return [None]  # Represent null nodes explicitly in the traversal
            result = []
            stack = [root]
            while stack:
                curr = stack.pop()
                if curr:
                    result.append(curr.val)
                    stack.append(curr.right)
                    stack.append(curr.left)
                else:
                    result.append(None)  # Add a marker for null nodes
            return result

        res1 = traverse(p)
        res2 = traverse(q)

        return res1 == res2