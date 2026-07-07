class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # multisorce bfs
        # look for "O" on the outer edges
        # run dfs/bfs from them 
        # add the (r, c) of found "O" to set
        # and add them to the bfs queue

        # iterate through the board
        # check if cell is "O" and is not in set of marked cells
        # if so, make it "X"

        q = deque()
        ROWS, COLS = len(board), len(board[0])
        og = set()

        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1) and board[r][c] == "O":
                    q.append((r, c))
                    og.add((r, c))

        visit = set()
        while q:
            r, c = q.popleft()
            if (r, c) in visit:
                continue
            visit.add((r, c))
            
            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == "O":
                    q.append((nr, nc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in visit:
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"






