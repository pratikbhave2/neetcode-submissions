# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # # REcursive inorder
        # def helper(root, res):
        #     if root == None:
        #         return res
            
        #     # Call helper on left first, append node and then call helper on right
        #     helper(root.left, res)
        #     res.append(root.val)
        #     helper(root.right, res)
        #     return res

        # res = []
        # res = helper(root, res)
        # print(res)
        # return res[k - 1]

        # Inorder iterative DFS
        result = []
        stack = [root]

        while len(stack) > 0:
            curr = stack.pop()
            if curr is not None:
                stack.append(curr.right)
                stack.append(curr)
                stack.append(curr.left)
            else:
                if len(stack) > 0:
                    result.append(stack.pop().val)
        return result[k-1]

