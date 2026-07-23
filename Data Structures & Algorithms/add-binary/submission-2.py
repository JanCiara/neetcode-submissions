class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n, m = len(a), len(b)
        res = ""
        carry = 0
        for i in range(max(n, m)):
            a_idx = n - 1 - i
            a_bit = a[a_idx] if a_idx >= 0 else 0
            
            b_idx = m - 1 - i
            b_bit = b[b_idx] if b_idx >= 0 else 0

            res_bit = carry ^ int(a_bit) ^ int(b_bit)

            carry = (int(a_bit) & int(b_bit)) | (int(a_bit) & carry) | (int(b_bit) & carry)

            res += str(res_bit)
        if carry:
            res += str(carry)
        return res[::-1]