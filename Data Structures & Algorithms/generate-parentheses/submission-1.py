class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # def isValid(p_string):
        #     left_count= 0
        #     for p in p_string:
        #         if p == "(":
        #             left_count += 1
        #         elif p == ")":
        #             left_count -= 1
        #         if left_count < 0:
        #             return False
        #     if left_count == 0:
        #         return True
        #     return False

        # q = collections.deque([""])
        # ans = []
        # while q:
        #     curr = q.popleft()

        #     if len(curr) == 2 * n:
        #         if isValid(curr):
        #             ans.append(curr)
        #         continue
        #     q.append(curr + ")")
        #     q.append(curr + "(")
        # return ans


        # DFS
        ans = []
        def helper(curr: str, left: int, right: int):
            if len(curr) == 2 * n:
                ans.append(curr)

            if left < n:
                helper(curr + "(", left + 1, right)
            if left > right:
                helper(curr + ")", left, right + 1)
        
        helper("", 0, 0)

        return ans