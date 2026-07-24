class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0 for _ in range(n + 1)]

        for i in range(n + 1):
            cur = 0
            for j in range(32):
                cur += (i >> j) & 1
            res[i] = cur

        return res