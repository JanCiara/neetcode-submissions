class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n + 1)]
        dp[0] = nums[0]

        for i in range(1, n):
            one = dp[i - 1]
            two = dp[i - 2] if i - 2 >= 0 else 0
            dp[i] = max(nums[i] + two, one)

        return dp[n - 1]