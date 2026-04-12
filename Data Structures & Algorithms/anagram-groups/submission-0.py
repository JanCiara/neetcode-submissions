class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def word_to_arr(w):
            arr = [0 for _ in range(26)]
            for c in w:
                idx = ord(c) - ord('a')
                arr[idx] += 1
            
            return arr
        
        mp = defaultdict(list)

        for s in strs:
            key = tuple(word_to_arr(s))
            mp[key].append(s)

        return list(mp.values())