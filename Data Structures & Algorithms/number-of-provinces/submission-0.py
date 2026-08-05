class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ROWS, COLS = len(isConnected), len(isConnected[0])
        adj = [[] for _ in range(ROWS)]
        res = 0
        seen = set()
        for r in range(ROWS):
            for c in range(COLS):
                if isConnected[r][c] == 1:
                    adj[r].append(c)

        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for nei in adj[node]:
                dfs(nei)

        for i in range(ROWS):
            if i not in seen:
                res += 1
                dfs(i)
        return res