class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0
        for c in s:
            lo += 1 if c == "(" else -1
            hi += 1 if c != ")" else -1
            if hi < 0:          # too many ')' even if all '*' are '('
                return False
            lo = max(lo, 0)     # lo can't go negative
        return lo == 0