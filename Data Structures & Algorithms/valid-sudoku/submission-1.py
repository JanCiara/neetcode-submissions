class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0 for _ in range(9)] for _ in range(9)]
        cols = [[0 for _ in range(9)] for _ in range(9)]
        squares = [[0 for _ in range(9)] for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                cur = int(board[r][c]) - 1
                if rows[r][cur] != 0:
                    return False
                rows[r][cur] = 1
                if cols[c][cur] != 0:
                    return False
                cols[c][cur] = 1
                if squares[((r // 3) * 3) + (c // 3)][cur] != 0:
                    return False
                squares[((r // 3) * 3) + (c // 3)][cur] = 1
        return True