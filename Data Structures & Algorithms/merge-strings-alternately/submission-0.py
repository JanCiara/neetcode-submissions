class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        l3 = l1+l2
        res = ['' for _ in range(l3)]
        
        x, y = 0, 0
        for i in range(l3):
            if x < l1 and (y == l2 or i % 2 == 0):
                res[i] = word1[x]
                x += 1
            else:
                res[i] = word2[y]
                y += 1


        return ''.join(res)