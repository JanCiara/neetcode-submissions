class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #dp top down
        cache = {} 
        def dfs(i, s):
            if (i, s) in cache:
                return cache[(i, s)]
            if i == len(nums):
                return 1 if s == target else 0
            
            cache[(i, s)] = dfs(i + 1, s + nums[i]) + dfs(i + 1, s - nums[i])
            return cache[(i, s)]
            
        return dfs(0, 0)