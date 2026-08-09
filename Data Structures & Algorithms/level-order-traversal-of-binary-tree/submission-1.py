# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res


        prev_level = -1

        q = deque([(root, 0)])
        level_res = [root.val]
        while q:
            curr, curr_level = q.popleft()
            if curr_level != prev_level:
                res.append(level_res)
                level_res = []

            if curr.left is not None:
                level_res.append(curr.left.val)
                q.append((curr.left, curr_level + 1))
            if curr.right is not None:
                level_res.append(curr.right.val)
                q.append((curr.right, curr_level + 1))

            prev_level = curr_level
        
        return res