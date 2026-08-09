class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        output = []

        def backtrack(i, curr, curr_sum):
            if curr_sum == target and curr not in output:
                output.append(curr[:])
                return

            if curr_sum > target or i >=n:
                return
            
            # if i > 0 and candidates[i] == candidates[i - 1]:
            #     return
            
            # include nums[i]
            curr.append(candidates[i])
            backtrack(i + 1, curr, curr_sum + candidates[i])
            curr.pop()
            backtrack(i + 1, curr, curr_sum)


        backtrack(0, [], 0)

        return output