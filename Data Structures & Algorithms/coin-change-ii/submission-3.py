class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]
        def dfs(i, a):
            if i == n or a < 0:
                return 0
            if a == 0:
                return 1
            if dp[i][a] != -1:
                return dp[i][a]

            res = 0
            for j in range(i, n):
                res += dfs(j, a - coins[j])         
            
            dp[i][a] = res
            return res
        return dfs(0, amount)