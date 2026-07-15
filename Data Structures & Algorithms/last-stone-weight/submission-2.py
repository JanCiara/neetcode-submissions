class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for s in stones:
            heapq.heappush(h, -s)
    

        while len(h) > 1:
            a, b = heapq.heappop(h), heapq.heappop(h)
            a *= -1
            b *= -1

            if a == b:
                continue
            elif a > b:
                heapq.heappush(h, -(a - b))
            else:
                heapq.heappush(h, -(b - a))

        return -h[-1] if h else 0