class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            cur_bit = (n >> i) & 1
            res |= cur_bit << (31 - i)
            res << 1

        return res