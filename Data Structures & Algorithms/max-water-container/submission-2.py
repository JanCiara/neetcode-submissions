class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        l = 0
        r = n - 1
        while l < r:
            cur = min(heights[l], heights[r]) * (r - l)
            res = max(res, cur)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res