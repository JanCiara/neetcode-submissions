class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        dp = {}
        if n + m != len(s3):
            return False

        def dfs(i, j):
            if i + j == len(s3):
                return True
            if (i, j) in dp:
                return dp[(i, j)]
            cur = s3[i + j]
            res = False

            if i < n and j < m and s1[i] == s2[j] == cur:
                res = dfs(i + 1, j) or dfs(i, j + 1)
            elif i < n and s1[i] == cur:
                res = dfs(i + 1, j)
            elif j < m and s2[j] == cur:
                res = dfs(i, j + 1)
            else:
                dp[(i, j)] = False
                return False
                
            dp[(i, j)] = res
            return res


        return dfs(0, 0)