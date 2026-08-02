class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = s[0]
        for i in range(n):
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r + 1]
                r += 1
                l -= 1
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r + 1]
                r += 1
                l -= 1
        return res
