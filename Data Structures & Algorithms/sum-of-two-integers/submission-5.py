class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0
        for i in range(32):
            a_bit = int(a >> i) & 1
            b_bit = int(b >> i) & 1

            cur_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit & b_bit) | (b_bit & carry) | (a_bit & carry) 

            res |= (cur_bit << i)
        
        if res >= (1 << 31):
            res -= (1 << 32)
        return res