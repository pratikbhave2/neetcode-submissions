class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Min heap -> Not optimal??
        stones = [-1 * stone for stone in stones] # Convert all to -ve to simulate max heap
        heapq.heapify(stones) # O(N) -> where N = len(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            y *= -1
            x *= -1
            if x < y:
                new_y = y - x
                heapq.heappush(stones, -new_y)

        if len(stones) > 0:
            return -1 * stones[-1]
        return 0
