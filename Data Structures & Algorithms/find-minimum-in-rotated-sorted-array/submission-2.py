class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mi = (l + r) // 2
            if nums[mi] > nums[r]:
                l = mi + 1   # min is strictly right of mi
            else:
                r = mi       # mi could be the min
        return nums[l]