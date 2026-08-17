class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        s = sum(stones)
        cur = [-1] * (s + 1)
        prev = cur[:]

        for i in range(n, -1, -1):
            for j in range(s, -1, -1):
                if i == n:
                    cur[j] = abs((sum(stones) - j) - j)
                else:
                    take = prev[j + stones[i]] if j + stones[i] <= s else float('inf')
                    not_take = prev[j]
                    cur[j] = min(
                        take, not_take
                    )
            prev, cur = cur, prev

        return prev[0]