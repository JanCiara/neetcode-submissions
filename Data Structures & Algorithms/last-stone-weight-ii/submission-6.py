class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        s = sum(stones)
        dp = [[-1] * (s + 1) for _ in range(n + 1)]

        for i in range(n, -1, -1):
            for j in range(s, -1, -1):
                if i == n:
                    dp[i][j] = abs((sum(stones) - j) - j)
                else:
                    take = dp[i + 1][j + stones[i]] if j + stones[i] <= s else float('inf')
                    not_take = dp[i + 1][j]
                    dp[i][j] = min(
                        take, not_take
                    )

        return dp[0][0]