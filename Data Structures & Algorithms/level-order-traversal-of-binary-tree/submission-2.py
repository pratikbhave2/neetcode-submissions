# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        res = []
        while len(q) > 0:
            qLen = len(q)
            lvl = []
            for i in range(qLen):
                curr = q.popleft()
                if curr:
                    lvl.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if len(lvl) > 0:
                res.append(lvl)
        
        return res