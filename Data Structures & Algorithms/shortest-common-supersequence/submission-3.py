class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        dp = [['' for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i == n:
                    dp[i][j] = str2[j:]
                elif j == m:
                    dp[i][j] = str1[i:]
                elif str1[i] == str2[j]:
                    dp[i][j] = str1[i] + dp[i + 1][j + 1]
                else:
                    s1 = dp[i + 1][j]
                    s2 = dp[i][j + 1]
                    if len(s1) < len(s2):
                        dp[i][j] = str1[i] + s1
                    else:
                        dp[i][j] = str2[j] + s2
        return dp[0][0]