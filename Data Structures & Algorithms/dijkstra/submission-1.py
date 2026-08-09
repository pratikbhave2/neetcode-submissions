class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}

        for i in range(n):
            adj[i] = []

        for source, dst, weight in edges:
            adj[source].append((dst, weight))

        shortest = {}
        min_heap = [(0, src)] # cost, node

        while min_heap:
            curr_cost, curr_node = heapq.heappop(min_heap)
            if curr_node in shortest:
                continue
            shortest[curr_node] = curr_cost
        
            for node, weight in adj[curr_node]:
                if node not in shortest:
                    heapq.heappush(min_heap, (weight + curr_cost, node))

        # fill in missing nodes
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1                    
        return shortest