class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        skipped = False
        while l < r:
            if s[l] != s[r]:
                if r - 1 == l:
                    return False if skipped else True
                if l + 2 < len(s) and s[l + 2] == s[r - 1] and s[l + 1] == s[r]:
                    l += 1
                    skipped = True
                elif r - 2 < len(s) and s[l + 1] == s[r - 2] and s[l] == s[r - 1]:
                    r -= 1
                    skipped = True
                else:
                    return False
            l += 1
            r -= 1
        return True