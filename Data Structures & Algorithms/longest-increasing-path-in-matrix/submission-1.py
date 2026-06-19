class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        res = 0
        ROWS, COLS = len(matrix), len(matrix[0])

        directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]

        def dfs(r, c, l):
            if not((0 <= r < ROWS) and (0 <= c < COLS)):
                return l
            if (r, c) in dp:
                return l + dp[(r, c)]
            
            cur = 0

            for x, y in directions:
                if not((0 <= r + x < ROWS) and (0 <= c + y < COLS)):
                    continue
                if matrix[r + x][c + y] > matrix[r][c]:
                    cur = max(cur, 1 + dfs(r + x, c + y, 0))

            dp[(r, c)] = cur
            return l + dp[(r, c)]

        for row in range(ROWS):
            for col in range(COLS):
                res = max(res, dfs(row, col, 1))

        return res