class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        negative = 1
        if x < 0:
            s = s[1:]
            negative = -1
        s=s[::-1]
        res = int(s)
        if res > 2**31 - 1:
            return 0
        return res * negative