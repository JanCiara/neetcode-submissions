class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reach = nums[0]

        for i in range(n):
            if reach < i:
                return False
            reach = max(reach, i + nums[i])

        return True