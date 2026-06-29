class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        toRot = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                elif grid[r][c] == 1:
                    toRot += 1
        
        time = rotten = 0
        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))
        while q:
            r, c, t = q.popleft()

            for nr, nc in dirs:
                if not(0 <= r + nr < ROWS and 0 <= c + nc < COLS) or grid[r + nr][c + nc] != 1:
                    continue
                grid[r + nr][c + nc] = 2
                rotten += 1
                q.append((r + nr, c + nc, t + 1))
                time = max(time, t + 1)

        return time if rotten == toRot else -1


