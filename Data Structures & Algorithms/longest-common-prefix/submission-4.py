class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x = strs[0]
        res = ""
        for i in range(len(x)):
            for s in strs:
                if s == "":
                    return ""
                if i == len(s) or x[i] != s[i]:
                    return res
            res += x[i]
        
        return res
