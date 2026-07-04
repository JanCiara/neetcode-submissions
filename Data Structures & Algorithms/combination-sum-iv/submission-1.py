class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for amount in range(1, target + 1):
            for num in nums:
                if num <= amount:
                    dp[amount] += dp[amount - num]
        return dp[target]