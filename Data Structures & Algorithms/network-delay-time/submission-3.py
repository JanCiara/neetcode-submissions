class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for s, d, t in times:
            adj[s].append((d, t))
        
        h = [(0, k)]
        dist = {}

        while h:
            time, node = heapq.heappop(h)
            if node in dist:
                continue
            dist[node] = time
            
            for nei, new_time in adj[node]:
                heapq.heappush(h, (time + new_time, nei))

        return max(dist.values()) if len(dist) == n else -1
