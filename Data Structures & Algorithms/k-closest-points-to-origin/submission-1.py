class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Brute force O(nlogn)
        # def sqrrootdistance(point):
        #     return ((point[0] * point[0]) + (point[1] * point[1])) ** (1/2)
        # points.sort(key = sqrrootdistance)
        # print(points)
        # return points[:k]

        # Max heap O(k∗logn)

        # heap = [-(sqrrootdistance(points[i])) for i in range(k)] 
        # heapq.heapify(heap)

        # for i in range(k, len(points)):
        #     dist = -sqrrootdistance(points[i])
        #     if dist > heap[0][0]:
        #         heapq.heappushpop(heap, (dist, i))
        
        # return [points[i] for (_, i) in heap]

        # Min heap: O (nlog n)

        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res