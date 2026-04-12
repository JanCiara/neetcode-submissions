class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()

        def dfs(idx, cur_sum, nums):
            if cur_sum == target:
                res.add(tuple(nums))
                return
            if cur_sum > target or idx == len(candidates):
                return
            # take
            nums.append(candidates[idx])
            dfs(idx + 1, cur_sum + candidates[idx], nums)   
            nums.pop()
            # not take
            while idx + 1 < len(candidates) and candidates[idx + 1] == candidates[idx]:
                idx += 1
            dfs(idx + 1, cur_sum, nums)
        
        dfs(0, 0, [])
        return [list(e) for e in res]