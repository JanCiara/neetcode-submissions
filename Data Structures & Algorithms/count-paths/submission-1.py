class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        dp[ROWS - 1][COLS - 1] = 1
        # dp[r][c] = dp(r + 1, c) + dp(r, c + 1)

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                bottom = dp[r + 1][c] if r + 1 < ROWS else 0
                right = dp[r][c + 1] if c + 1 < COLS else 0
        
                dp[r][c] += bottom + right

        return dp[0][0]