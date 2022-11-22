from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        changedM, changedN = [False] * m, [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    changedM[i] = changedN[j] = True

        for i in range(m):
            for j in range(n):
                if changedM[i] or changedN[j]:
                    matrix[i][j] = 0


def polyfill(matrix: List[List[int]]):
    Solution().setZeroes(matrix)
    print(matrix)


# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
polyfill([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
polyfill([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
