class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        seen = set()
        for i in range(len(edges)):
            u, v = edges[i]
            adj[u].append(v)
            adj[v].append(u)

        def dfs(cur, prev):
            # cycle
            if cur in seen:
                return True

            seen.add(cur)
            for u in adj[cur]:
                if u == prev:
                    continue
                if dfs(u, cur):
                    return True

            return False
            
        return not dfs(0, -1) and len(seen) == n

        