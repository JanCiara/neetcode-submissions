class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        n = len(nums)
        target = s // 2
        dp = [None] * (target + 1)
        dp[0] = True
        
        for i in range(n - 1, -1, -1):                
            for t in range(target, -1, -1):
                a = dp[t]
                b = dp[t - nums[i]] if t - nums[i] >= 0 else False
                dp[t] = a or b

        return dp[target]