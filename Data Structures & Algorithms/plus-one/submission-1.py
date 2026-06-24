class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        end = -1
        for i in range(n):
            cur = digits[n - i - 1]
            if cur == 9:
                digits[n - i - 1] = 0
                end = i
            else:
                digits[n - i - 1] += 1
                break

        return [1] + digits if end == n - 1 else digits