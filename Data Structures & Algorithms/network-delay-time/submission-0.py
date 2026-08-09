class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build adjacency list
        adj = {}

        for i in range(1, n + 1):
            adj[i] = []

        for src, dst, time in times:
            adj[src].append((dst, time))

        min_heap = [(0, k)] # time, first node to send the signal
        visit = set()
        total_time = 0
        while min_heap:
            curr_time, curr_node = heapq.heappop(min_heap)
            if curr_node in visit:
                continue

            visit.add(curr_node)
            # total time = curr time because curr_time is the shortest time needed
            # to reach all signals till this point
            total_time = curr_time

            for node, time in adj[curr_node]:
                if node not in visit:
                    heapq.heappush(min_heap, (curr_time + time, node))
        

        return total_time if len(visit) == n else -1