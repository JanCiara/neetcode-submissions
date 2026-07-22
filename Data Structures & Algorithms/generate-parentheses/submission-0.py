class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        def dfs(o, c):
            if c > o:
                return
            if o + c == 2 * n:
                if o == c:
                    res.append("".join(cur[:]))
                return
            
            cur.append("(")
            dfs(o + 1, c)
            cur.pop()

            cur.append(")")
            dfs(o, c + 1)
            cur.pop()

        dfs(0, 0)
        return res