class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        res = 0
        dp = {} # idx, sum : res
        total = sum(stones)
        target = (total + 1) // 2

        def dfs(i, s):
            if i == len(stones) or s >= target:
                return abs(s - (total - s))
            if (i, s) in dp:
                return dp[(i, s)]
            
            dp[(i, s)] = min(dfs(i + 1, s + stones[i]), 
                             dfs(i + 1, s))
            return dp[(i, s)]

        return dfs(0, 0)