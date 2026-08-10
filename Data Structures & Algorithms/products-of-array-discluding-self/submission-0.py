class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0 for _ in range(n)]
        sufix = prefix[:]

        cur = 1
        for i in range(n):
            cur *= nums[i]
            prefix[i] = cur
        
        cur = 1
        for i in range(n - 1, -1, -1):
            cur *= nums[i]
            sufix[i] = cur
        
        res = [0 for _ in range(n)]
        for i in range(n):
            left = prefix[i - 1] if i - 1 >= 0 else 1
            right = sufix[i + 1] if i + 1 < n else 1

            res[i] = left * right

        return res