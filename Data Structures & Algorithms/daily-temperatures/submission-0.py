class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        n = len(temperatures)
        res = [0 for _ in range(n)]

        for i, temp in enumerate(temperatures):
            while s and s[-1][0] < temp:
                _, idx = s.pop()
                res[idx] = i - idx
            s.append((temp, i))

        return res