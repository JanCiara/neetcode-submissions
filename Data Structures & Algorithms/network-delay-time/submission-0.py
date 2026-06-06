class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))      # lista sasiedztwa, NIE nadpisujemy

        dist = {}                       # node -> najkrotszy czas dotarcia
        heap = [(0, k)]                 # (czas, wezel)

        while heap:
            time, node = heapq.heappop(heap)
            if node in dist:            # juz finalnie odwiedzony -> pomijamy
                continue
            dist[node] = time
            for nei, w in adj[node]:
                if nei not in dist:
                    heapq.heappush(heap, (time + w, nei))

        return max(dist.values()) if len(dist) == n else -1