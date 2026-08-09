class Solution:
    def jump(self, nums: List[int]) -> int:
        # BFS on 1 D array (GREEDY)
        # O(N) TIme, O(1) space
        # How O(N) time? each index is processed only once
        # while loop runs at the max O(N) times, because right strictly increases, we never re-visit 
        # the same index.
        # Inner loop will run max of O(N) times
        # While loop and for loop are mutualy exclusive (NEver happen that both of them run simulatenously)
        # for O(N) each
        # Simplified BFS using 2 pointers
        num_jumps = 0
        left, right = 0, 0 # This will tell us our window based on number of jumps that we take

        while right < len(nums) - 1:
            farthest_jump = 0 # To keep track of who among left, right index can jump the longest
            # Going through this loop to find who can jump farthest (left or right) and 
            # then update left and right to new values
            for i in range(left, right + 1):
                farthest_jump = max(farthest_jump, i + nums[i])
            left = right + 1
            right = farthest_jump
            num_jumps += 1
        return num_jumps
