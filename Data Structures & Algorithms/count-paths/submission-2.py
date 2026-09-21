class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        cur = [0 for _ in range(COLS)]
        prev = cur[:]
        prev[COLS - 1] = 1
        
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                bottom = prev[c]
                right = cur[c + 1] if c + 1 < COLS else 0
        
                cur[c] = bottom + right
            prev, cur = cur, prev

        return prev[0]