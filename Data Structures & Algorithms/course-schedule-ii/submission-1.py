class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[a].append(b)
        
        visit = [0] * numCourses # 0 not-visited 
                    #1 on path 2 visited(no cycle from this)
        def dfs(i):
            if visit[i] == 1: # cycle
                return True
            if visit[i] == 2:
                return False
            visit[i] = 1
            for nei in adj[i]:
                if dfs(nei):
                    return True

            visit[i] = 2
            res.append(i)
            return False

        return [] if any(dfs(i) for i in range(numCourses)) else res