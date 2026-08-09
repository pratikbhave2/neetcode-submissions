# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Recursion
        # def isValid(node: TreeNode, left: float, right: float):
        #     if not node:
        #         return True
            
        #     if not (left < node.val < right):
        #         return False
            
        #     return isValid(node.left, left, node.val) and isValid(node.right, node.val, right)
        # return isValid(root, float('-inf'), float('inf'))

            
        # iterative BFS

        if not root:
            return True
        
        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, left, right = q.popleft()
            if not (left < node.val < right):
                return False
            
            if node.left:
                q.append((node.left, left, node.val))
            
            if node.right:
                q.append((node.right, node.val, right))
        return True