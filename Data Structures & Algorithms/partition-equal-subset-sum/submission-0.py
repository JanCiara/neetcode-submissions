class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        h = s / 2
        n = len(nums)

        def dfs(curSum, i):
            if curSum > h or i == n:
                return False
            if curSum == h:
                return True
            r = False
            if curSum + nums[i] <= h:
                r = dfs(curSum + nums[i], i + 1)
            return r or dfs(curSum, i + 1)

        return dfs(0, 0)
