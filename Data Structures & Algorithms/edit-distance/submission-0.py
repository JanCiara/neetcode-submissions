class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        n, m = len(word1), len(word2)
        def dfs(i, j):
            if i == n:
                return m - j
            if j == m:
                return n - i
            
            if (i, j) in cache:
                return cache[(i, j)]

            if word1[i] == word2[j]:
                res = dfs(i + 1, j + 1)
            else:
                res = min(dfs(i + 1, j), dfs(i + 1, j + 1), dfs(i, j + 1))
                res += 1

            cache[(i, j)] = res
            return res

        return dfs(0, 0)