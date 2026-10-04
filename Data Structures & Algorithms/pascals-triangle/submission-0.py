class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        for row in range(numRows):
            cur_row = []
            for i in range(row + 1):
                if i == 0 or i == row:
                    cur = 1
                else:
                    cur = res[row - 1][i - 1] + res[row - 1][i]
                cur_row.append(cur)
            res.append(cur_row)

        return res