class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(i):
            if i == 0:
                return 1
            if i in memo:
                return memo[i]

            one = dfs(i - 1)
            two = dfs(i - 2) if i - 2 >= 0 else 0
            memo[i] = one + two
            return one + two

        return dfs(n)