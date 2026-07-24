class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        idx = 1
        k = 1 
        for i in range(1, len(nums)):
            if nums[k - 1] != nums[i]:
                nums[k] = nums[i]
                k += 1
        return k