class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        n = len(digits)
        cur = []
        def dfs(i):
            if i == n:
                res.append(''.join(cur[:]))
                return    

            for c in digitToChar[digits[i]]:
                cur.append(c)
                dfs(i + 1)
                cur.pop()

        dfs(0)
        return res