class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = 0
        max_count = max(c.values())

        for k, v in c.items():
            if v == max_count:
                return k

        return res