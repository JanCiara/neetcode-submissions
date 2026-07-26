class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [float('inf') for _ in range(n)]
        def dfs(i):
            if i == n:
                return 0
            if dp[i] < float('inf'):
                return dp[i]
            one_step = dfs(i + 1)
            two_step = 0
            if i + 2 <= n:
                two_step = dfs(i + 2)
            dp[i] = cost[i] + min(one_step, two_step)
            return dp[i]

        return min(dfs(0), dfs(1))