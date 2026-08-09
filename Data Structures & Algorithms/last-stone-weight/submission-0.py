class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # O (n log n)
        # Convert all stones to negative values to simulate a max-heap using a min-heap
        stones = [-stone for stone in stones]
        heapq.heapify(stones)  # Transform the list into a heap

        while len(stones) > 1:
            # Extract the two heaviest stones
            heaviest = -heapq.heappop(stones)
            second_heaviest = -heapq.heappop(stones)

            if heaviest != second_heaviest:
                # If they are not the same, push the difference back into the heap
                heapq.heappush(stones, -(heaviest - second_heaviest))

        if stones:
            return -stones[0]

        else:
            return 0