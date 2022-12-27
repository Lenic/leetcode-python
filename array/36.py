from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidInRow(i: int, j: int) -> bool:
            val = board[i][j]
            for k, item in enumerate(board[i]):
                if item == val and k != j:
                    return False
            return True

        def isValidInColumn(i: int, j: int) -> bool:
            val = board[i][j]
            for k in range(9):
                if board[k][j] == val and k != i:
                    return False
            return True

        def isValidInRect(i: int, j: int) -> bool:
            val, ir, ic = board[i][j], i // 3, j // 3
            for x in range(ir * 3, (ir + 1) * 3):
                for y in range(ic * 3, (ic + 1) * 3):
                    if board[x][y] == val and x != i and y != j:
                        return False
            return True

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    isValid = isValidInColumn(i, j) and isValidInRow(i, j) and isValidInRect(i, j)
                    if not isValid:
                        return False
        return True


# false
print(
    Solution().isValidSudoku(
        board=[
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)

# true
print(
    Solution().isValidSudoku(
        board=[
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
