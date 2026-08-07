class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        S = sum(nums)
        if abs(target) > S:
            return 0
        prev = [0] * (2 * S + 1)
        cur = prev[:]
        for i in range(n, -1, -1):
            for t in range(-S, S + 1):
                if i == n:
                    cur[S + t] = 1 if t == 0 else 0
                else:
                    a = prev[S + t - nums[i]] if 0 <= S + t - nums[i] < 2 * S + 1 else 0
                    b = prev[S + t + nums[i]] if 0 <= S + t + nums[i] < 2 * S + 1 else 0
                    cur[S + t] = a + b
            cur, prev = prev, cur

        return prev[target + S]