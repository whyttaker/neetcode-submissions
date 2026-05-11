class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        for i in range(9):
            nums = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in nums:
                    return False
                nums.add(board[i][j])

        
        for i in range(9):
            nums = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in nums:
                    return False
                nums.add(board[j][i])

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                nums = set()
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in nums:
                            return False
                        nums.add(board[i][j])

        return True