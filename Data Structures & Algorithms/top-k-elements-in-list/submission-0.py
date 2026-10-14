class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        h = []
        for number, count in counter.items():
            heapq.heappush(h, (count, number))
            if len(h) > k:
                heapq.heappop(h)
        
        res = []
        for i in range(len(h)):
            res.append(heapq.heappop(h)[1])

        return res