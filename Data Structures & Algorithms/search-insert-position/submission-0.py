class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            mi = (l + r) // 2

            if nums[mi] == target:
                return mi
            elif nums[mi] > target:
                r = mi - 1
            else:
                l = mi + 1

        return l