class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = math.ceil(sum(stones) / 2)
        other = math.floor(abs(sum(stones) - target))
        dp = [[-1] * (sum(stones) + 1) for _ in range(len(stones) + 1)]


        def dfs(i, cur):
            if i == len(stones):
                dp[i][cur] = abs((sum(stones) - cur) - cur)
                return dp[i][cur]

            if dp[i][cur] != - 1:
                return dp[i][cur]

            dp[i][cur] = min(
                dfs(i + 1, cur + stones[i]),
                dfs(i + 1, cur)
            )
            return dp[i][cur]


        return dfs(0, 0)