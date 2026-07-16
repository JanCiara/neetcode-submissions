class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        cur = []
        seen = set()
        def dfs(idx):
            if len(cur) == n:
                res.append(cur[:])
                return
            
            for i in range(0, n):
                if nums[i] in seen:
                    continue
                cur.append(nums[i])
                seen.add(nums[i])
                dfs(i + 1)
                cur.pop()
                seen.remove(nums[i])
        dfs(0)
        return res