class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # (O N Log N) Time and O(N) space
        stones = [-1 * stone for stone in stones] # Convert all to -ve to simulate max heap
        heapq.heapify(stones) # O(N) -> where N = len(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            # Given condition is y > x then new_y = y - x
            # but since we are simulating -ve, we check for 
            # x > y and new_y = x - y
            if x > y:
                new_y = x - y
                heapq.heappush(stones, -new_y)

        if len(stones) > 0:
            return -1 * stones[-1]
        return 0
