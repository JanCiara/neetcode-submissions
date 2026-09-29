class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            adj[a].append(b)
        seen = set()
        done = set()
        def dfs(i):
            if i in seen:
                return True
            if i in done:
                return False
            seen.add(i)
            for nei in adj[i]:
                if dfs(nei):
                    return True
            seen.remove(i)
            done.add(i)
            return False

        for x in range(numCourses):
            if dfs(x):
                return False
        return True
