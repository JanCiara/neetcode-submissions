class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(nums):
            n = len(nums)
            dp = [0 for _ in range(n)]

            for i in range(n - 1, -1, -1):
                a = nums[i] + dp[i + 2] if i + 2 <= n - 1 else nums[i]
                b = dp[i + 1] if i + 1 <= n - 1 else 0
                dp[i] = max(a, b)

            return dp[0]
        return max(helper(nums[1:]), helper(nums[:-1]))