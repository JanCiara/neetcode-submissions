class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        c1, c2 = [0] * 26, [0] * 26
        for c in s1:
            c1[ord(c) - ord('a')] += 1
        for c in s2[:len(s1)]:
            c2[ord(c) - ord('a')] += 1
        
        matches = sum(1 for i in range(26) if c1[i] == c2[i])
        
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            idx_in = ord(s2[i]) - ord('a')
            idx_out = ord(s2[i - len(s1)]) - ord('a')
            
            c2[idx_in] += 1
            if c2[idx_in] == c1[idx_in]:
                matches += 1
            elif c2[idx_in] == c1[idx_in] + 1:
                matches -= 1
            
            c2[idx_out] -= 1
            if c2[idx_out] == c1[idx_out]:
                matches += 1
            elif c2[idx_out] == c1[idx_out] - 1:
                matches -= 1
        
        return matches == 26