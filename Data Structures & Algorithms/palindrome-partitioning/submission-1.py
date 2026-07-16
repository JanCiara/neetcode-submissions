class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(a):
            return a == a[::-1]
        n = len(s)
        res = []
        cur = []
        def dfs(idx):
            if idx == n:
                res.append(cur[:])
                return
            for e in range(idx, n):
                if isPalindrome(s[idx:e + 1]):
                    cur.append(s[idx:e + 1])
                    dfs(e + 1)
                    cur.pop()
        dfs(0)
        return res