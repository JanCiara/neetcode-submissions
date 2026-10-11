class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(cur_sum):
            if cur_sum == target:
                return 1
            if cur_sum > target:
                return 0
            if cur_sum in cache:
                return cache[cur_sum]
            res = 0
            for i in range(len(nums)):
                res += dfs(cur_sum + nums[i])
            cache[cur_sum] = res
            return res

        return dfs(0)