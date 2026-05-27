class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])

        n = len(intervals)
        if n == 1:
            return intervals
        res = []
        prev = intervals[0]

        for i in range(1, n):
            cur = intervals[i]
            if prev[1] < cur[0]:
                res.append(prev)
                prev = cur
            else:
                prev[1] = max(cur[1], prev[1])
            
            if i == n - 1:
                res.append(prev)

        return res