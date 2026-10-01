class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for n in nums:
            if n - 1 in s:
                continue
            tmp = n
            x = 0
            while tmp + x in s:
                res = max(res, x + 1)
                x += 1

        return res