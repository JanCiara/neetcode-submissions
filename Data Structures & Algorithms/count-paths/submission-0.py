class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        dp[ROWS - 1][COLS - 1] = 1
        # dp[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
        def dfs(r, c):
            if not(0 <= r < ROWS and 0 <= c < COLS):
                return 0
            if dp[r][c] != 0:
                return dp[r][c]
            dp[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
            return dp[r][c]

        return dfs(0, 0)