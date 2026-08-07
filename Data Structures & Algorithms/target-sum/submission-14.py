class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        S = sum(nums)
        if abs(target) > S:
            return 0
        dp = [[-1] * (2 * S + 1) for _ in range(n + 1)]
        
        for i in range(n, -1, -1):
            for t in range(-S, S + 1):
                if i == n:
                    dp[i][S + t] = 1 if t == 0 else 0
                else:
                    a = dp[i + 1][S + t - nums[i]] if 0 <= S + t - nums[i] < 2 * S + 1 else 0
                    b = dp[i + 1][S + t + nums[i]] if 0 <= S + t + nums[i] < 2 * S + 1 else 0
                    dp[i][S + t] = a + b

        return dp[0][target + S]