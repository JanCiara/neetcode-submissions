class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]
        h = [] # min heap
        heapq.heappush(h, (0, k))
        for u, v, t in times:
            adj[u].append((v, t))
        
        reached = 0
        time = 0
        seen = set()
        while h:
            t, u = heapq.heappop(h)
            if u in seen:
                continue
            reached += 1
            time = t
            seen.add(u)
            for nei, w in adj[u]:
                heapq.heappush(h, (t + w, nei))
                

        return time if reached == n else -1