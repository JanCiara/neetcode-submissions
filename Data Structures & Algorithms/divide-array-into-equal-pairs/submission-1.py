class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        s = set()

        for n in nums:
            if n not in s:
                s.add(n)
            else:
                s.remove(n)

        return not s