class Solution:
    def maxDepth(self, s: str) -> int:
        stack = 0
        res = 0
    
        for i in s:
            if i == "(":
                stack+=1
                res = max(res, stack)
            elif i == ")":
                stack-=1
            

        return res