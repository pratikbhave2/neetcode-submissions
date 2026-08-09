class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        n = len(nums)

        def backtrack(i, curr, curr_sum):
            if curr_sum == target:
                output.append(curr[:])
                return
            
            if curr_sum > target or i >=n:
                return
            
            curr.append(nums[i])
            backtrack(i, curr, curr_sum + nums[i])
            curr.pop()

            backtrack(i + 1, curr, curr_sum)




        backtrack(0, [], 0)
    
        return output


