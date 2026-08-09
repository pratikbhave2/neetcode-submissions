# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(root: TreeNode):
            if not root:
                return 0

            nonlocal diameter
            left_dia = dfs(root.left)
            right_dia = dfs(root.right)

            diameter = max(diameter, left_dia + right_dia)

            return max(left_dia, right_dia) + 1
        dfs(root)
        return diameter