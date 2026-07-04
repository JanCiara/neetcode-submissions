class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(total):
            if total > target:
                return 0
            if total == target:
                return 1
            if total in dp:
                return dp[total]

            res = 0
            for i in range(len(nums)):
                res += dfs(total + nums[i])
            dp[total] = res
            return res

        return dfs(0)