class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = r = 0
        while r < len(nums) - 1:
            cur_max = 0
            for i in range(l, r + 1):
                cur_max = max(cur_max, i + nums[i])
            l, r = r + 1, cur_max
            jumps += 1

        return jumps