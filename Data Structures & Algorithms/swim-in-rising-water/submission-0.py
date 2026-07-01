class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        min_heap = [(grid[0][0], (0, 0))] # max lvl so far, (r, c)

        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        visit = set()
        while min_heap:
            lvl, (r, c) = heapq.heappop(min_heap)
            if (r, c) in visit:
                continue
            visit.add((r, c))
            if r == ROWS - 1 and c == COLS - 1:
                return lvl

            for (nr, nc) in dirs:
                if 0 <= nr + r < ROWS and 0 <= nc + c < COLS:
                    max_lvl = max(lvl, grid[nr + r][nc + c])
                    heapq.heappush(min_heap, (max_lvl, (nr + r, nc + c)))
        return 0