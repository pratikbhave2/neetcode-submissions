class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Using indegree: O(V + E) time + space
        # Topological sort
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        output = []
        while q:
            node = q.popleft()
            finish += 1
            output.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if finish != numCourses:
            return []
        return output[::-1]


        # Using DFS topological sort
        # adj = [[] for i in range(numCourses)]
        # indegree = [0] * numCourses
        # for nxt, pre in prerequisites:
        #     indegree[nxt] += 1
        #     adj[pre].append(nxt)
        
        # output = []

        # def dfs(node):
        #     output.append(node)
        #     indegree[node] -= 1
        #     for nei in adj[node]:
        #         indegree[nei] -= 1
        #         if indegree[nei] == 0:
        #             dfs(nei)
        
        # for i in range(numCourses):
        #     if indegree[i] == 0:
        #         dfs(i)
        
        # return output if len(output) == numCourses else []
