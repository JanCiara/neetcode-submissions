class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        cache = {}
        def dfs(l, r):
            if l == -1 or r == n:
                return 0
            if (l, r) in cache:
                return cache[(l, r)]

            if s[l] == s[r]:
                length = 1 if l == r else 2
                cache[(l, r)] = length + dfs(l - 1, r + 1)
            else:
                cache[(l, r)] = max(
                    dfs(l - 1, r),
                    dfs(l, r + 1)
                )
            return cache[(l, r)]
        res = 0
        for i in range(n):
            res = max(
                res,
                dfs(i, i),
                dfs(i, i + 1)
            )
        return res