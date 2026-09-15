class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topolpogical sort

        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for src, dst in prerequisites:
            adj[src].append(dst)
            indegree[dst] += 1
        
        # find nodes where indegree for that node = 0
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        res = []
        while q:
            node = q.popleft()
            finish += 1
            res.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return res[::-1] if numCourses==finish else []