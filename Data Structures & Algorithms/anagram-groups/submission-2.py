class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for s in strs:
            key = sorted(s)
            mp[tuple(key)].append(s)

        return list(mp.values())