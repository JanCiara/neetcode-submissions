class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums) % 2 != 0:
            return False
        for i in range(1, len(nums), 2):
            a, b = nums[i - 1], nums[i]
            if a != b:
                return False
        return True