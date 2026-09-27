class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        ans = 0
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def dfs(r, c):
            if (
                not (0 <= r < ROWS and 0 <= c < COLS)
                or grid[r][c] != 1
                or (r, c) in seen
            ):
                return 0
            seen.add((r, c))
            res = 1
            for dr, dc in DIRS:
                nr, nc = dr + r, dc + c
                res += dfs(nr, nc)
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in seen:
                    ans = max(ans, dfs(r, c))

        return ans
