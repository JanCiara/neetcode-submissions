class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        cur = [0] * (amount + 1)
        cur[0] = 1
        prev = cur[:]

        for i in range(n - 1, -1, -1):
            for j in range(1, amount + 1):
                cur[j] = prev[j]
                if j - coins[i] >= 0:
                    cur[j] += cur[j - coins[i]]
            prev, cur = cur, prev
        return prev[amount]