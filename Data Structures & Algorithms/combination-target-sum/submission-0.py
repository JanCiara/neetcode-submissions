class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(idx, cur_sum, seq):
            if idx == len(nums) or cur_sum > target:
                return
            if cur_sum == target:
                res.append(seq)
                return 

            dfs(idx, cur_sum + nums[idx], seq + [nums[idx]])
            dfs(idx + 1, cur_sum, seq)

        dfs(0, 0, [])
        return res