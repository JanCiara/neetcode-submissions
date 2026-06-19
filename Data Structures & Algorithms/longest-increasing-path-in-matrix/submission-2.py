class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]

            best = 1
            for x, y in directions:
                nr, nc = r + x, c + y
                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))

            dp[(r, c)] = best
            return best

        return max(dfs(r, c) for r in range(ROWS) for c in range(COLS))