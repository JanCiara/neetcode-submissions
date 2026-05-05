class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        h = s // 2
        n = len(nums)
        memo = [[-1] * (h + 1) for _ in range(n + 1)]

        def dfs(curSum, i):
            if curSum > h or i == n:
                return False
            if curSum == h:
                return True
            if memo[i][curSum] != -1:
                return memo[i][curSum]

            r = False
            if curSum + nums[i] <= h:
                r = dfs(curSum + nums[i], i + 1)

            memo[i][curSum] = r or dfs(curSum, i + 1)

            return memo[i][curSum]

        return dfs(0, 0)
