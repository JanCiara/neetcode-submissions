class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(a):
            return a == a[::-1]
        n = len(s)
        res = []
        def dfs(idx, cur, e):
            if idx == n - 1:
                if isPalindrome(e + s[idx]):
                    res.append(cur + [e + s[idx]])
                return
            
            if isPalindrome(e + s[idx]):
                dfs(idx + 1, cur + [e + s[idx]], "")
            dfs(idx + 1, cur, e + s[idx])

        dfs(0, [], "")
        return res