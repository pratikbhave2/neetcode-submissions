class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                if i > hashmap[diff]:
                    return [hashmap[diff], i]
                else:
                    return [i, hashmap[diff]] 
            else:
                hashmap[nums[i]] = i

