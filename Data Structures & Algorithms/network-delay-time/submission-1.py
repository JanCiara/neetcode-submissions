class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = {}
        con = {i : [] for i in range(n + 1)}

        for node, d, t in times:
            con[node].append([d, t])

        h = [(0, k)]

        while h:
            cur_time, cur = heapq.heappop(h)
            if cur in dist:
                continue
            dist[cur] = cur_time
            for nei, new_time in con[cur]:
                if nei in dist:
                    continue
                heapq.heappush(h, [cur_time + new_time, nei])
            

        return max(dist.values()) if len(dist) == n else -1