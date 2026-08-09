class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # O(nlogk)
        # Logic : store only those numbers starting with k largest
        # as the minimum in the heap
        # so that you can quickly return heap[0]
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]