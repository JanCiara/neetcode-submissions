class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #brute force
        def dfs(i, s):
            if i == len(nums):
                return 1 if s == target else 0
            
            return dfs(i + 1, s + nums[i]) + dfs(i + 1, s - nums[i])
        
        return dfs(0, 0)