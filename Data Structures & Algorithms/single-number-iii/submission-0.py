class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        
        dif = 1
        while not (dif & xor):
            dif = dif << 1
        
        a = b = 0
        for n in nums:
            if n & dif:
                a ^= n
            else:
                b ^= n

        return [a, b]