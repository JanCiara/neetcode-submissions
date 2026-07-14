class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        l, r = 0, n - 1

        while l <= r:
            mi = l + (r - l) // 2

            if nums[mi] > nums[mi + 1]:
                return nums[mi + 1]
            elif nums[mi] > nums[n - 1]:
                l = mi + 1
            else:
                r = mi - 1

        return nums[l]