class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[-1 for _ in range(n)] for _ in range(n)]

        def dfs(i, j):
            if j < i:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if i == j:
                dp[i][j] = 1
            elif s[i] == s[j]:
                dp[i][j] = 2 + dfs(i + 1, j - 1)
            else:
                dp[i][j] = max(
                    dfs(i + 1, j),
                    dfs(i, j - 1)
                )
            return dp[i][j]

        return dfs(0, n - 1)