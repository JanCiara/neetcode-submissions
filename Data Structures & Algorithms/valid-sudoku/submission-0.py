class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False for _ in range(9)] for _ in range(9)]
        cols = [[False for _ in range(9)] for _ in range(9)]
        boxes = [[False for _ in range(9)] for _ in range(9)]

        for row in range(9):
            for col in range(9):
                cur = board[row][col]
                if cur == ".":
                    continue
                cur = ord(cur) - ord('0') - 1
                if rows[row][cur] == True:
                    return False
                if cols[col][cur] == True:
                    return False
                box_idx = (row // 3) * 3 + (col // 3)
                if boxes[box_idx][cur] == True:
                    return False
                
                rows[row][cur] = True
                cols[col][cur] = True
                boxes[box_idx][cur] = True
        return True