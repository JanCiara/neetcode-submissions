class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        cur = [0 for _ in range(n)]
        prev = cur[:]
        for i in range(n - 1, -1, -1):
            cur[i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    cur[j] = 2 + prev[j - 1]
                else:
                    cur[j] = max(
                        prev[j],
                        cur[j - 1]
                    )
            cur, prev = prev, cur


        return prev[n - 1]

