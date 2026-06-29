class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS*COLS - 1
    
        while l <= r:
            mi = l + (r - l) // 2
            nc = mi % COLS
            nr = mi // COLS

            val = matrix[nr][nc]
            if val == target:
                return True
            elif val < target:
                l = mi + 1
            else:
                r = mi - 1

        return False