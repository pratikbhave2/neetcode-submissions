# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # # Brute force (dfs iterative)
        # # Handle null cases upfront
        # if not p and not q:
        #     return True
        # if not p or not q:
        #     return False

        # # Brute force: Compare Pre-order traversal lists
        # def traverse(root):
        #     if not root:
        #         return [None]  # Represent null nodes explicitly in the traversal
        #     result = []
        #     stack = [root]
        #     while stack:
        #         curr = stack.pop()
        #         if curr:
        #             result.append(curr.val)
        #             stack.append(curr.right)
        #             stack.append(curr.left)
        #         else:
        #             result.append(None)  # Add a marker for null nodes
        #     return result

        # res1 = traverse(p)
        # res2 = traverse(q)

        # return res1 == res2

        # Recursion
        # if not p and not q:
        #     return True

        # if not p or not q or p.val != q.val:
        #     return False

        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # Smart iterative

        # Use stacks to traverse both trees
        stack = [(p, q)]
        
        while stack:
            node1, node2 = stack.pop()
            # If both are None, continue
            if not node1 and not node2:
                continue
            # If one is None or the values differ, trees are not the same
            if not node1 or not node2 or node1.val != node2.val:
                return False
            # Push left and right children of both nodes to the stack
            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))
        
        return True