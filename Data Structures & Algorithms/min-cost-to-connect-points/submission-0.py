class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i : [] for i in range(n)} # node : [(cost, node), ...]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                px, py = points[i]
                x, y = points[j]
                cost = abs(px - x) + abs(py - y)
                adj[i].append((cost, j))
        
        min_heap = [[0, 0]] # (cost, node)
        seen = set()
        res = 0
        while len(seen) < n:
            cost, node = heapq.heappop(min_heap)
            if node in seen:
                continue
            res += cost
            seen.add(node)
            for new_cost, new_node in adj[node]:
                heapq.heappush(min_heap, [new_cost, new_node])                
            
        
        return res

