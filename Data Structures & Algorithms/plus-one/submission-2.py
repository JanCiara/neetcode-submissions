class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n):
            cur = digits[n - i - 1]
            if cur == 9:
                digits[n - i - 1] = 0
            else:
                digits[n - i - 1] += 1
                return digits

        return [1] + digits