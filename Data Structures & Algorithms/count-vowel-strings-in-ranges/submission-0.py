class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        n = len(words)
        prefix = [0 for _ in range(n)]
        cur = 0
        for i, w in enumerate(words):
            if w[0] in vowels and w[-1] in vowels:
                cur += 1
            prefix[i] = cur
        
        res = []
        for b, e in queries:
            end_sum = prefix[e]
            begin_sum = prefix[b - 1] if b - 1 >= 0 else 0
            res.append(end_sum - begin_sum)

        return res