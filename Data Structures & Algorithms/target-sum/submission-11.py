class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        S = sum(nums)
        if abs(target) > S:
            return 0
        dp = [[-1] * (2 * S + 1) for _ in range(n)]

        def dfs(i, t):
            if i == n:
                return 1 if t == 0 else 0
            if abs(t) > S:
                return 0
            if dp[i][t + S] != -1:
                return dp[i][t + S]
            dp[i][t + S] = dfs(i + 1, t - nums[i]) + dfs(i + 1, t + nums[i])
            return dp[i][t + S]

        return dfs(0, target)