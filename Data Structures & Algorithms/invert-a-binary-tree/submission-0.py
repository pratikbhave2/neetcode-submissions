# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if not root:
        #     return None

        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root


        # Iterative DFS
        if not root:
            return None
        stack = [root]
        while len(stack) > 0:
            curr = stack.pop()

            curr.left, curr.right = curr.right, curr.left
            if curr.left is not None:
                stack.append(curr.left)
            
            if curr.right is not None:
                stack.append(curr.right)
        return root

