class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ext = set()
        res = 0
        l = r = 0

        while r < n:
            cur = s[r]
            while cur in ext and l < n:
                ext.remove(s[l])
                l += 1
            ext.add(s[r])
            r += 1
            res = max(res, len(ext))

        return res