class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        n = len(nums)
        target = s // 2
        dp = [[None] * (target + 1) for _ in range(n + 1)]
        dp[n][0] = True
        for i in range(n - 1, -1, -1):                
            for t in range(target + 1):
                a = dp[i + 1][t]
                b = dp[i + 1][t - nums[i]] if t - nums[i] >= 0 else False
                dp[i][t] = a or b

        return dp[0][target]