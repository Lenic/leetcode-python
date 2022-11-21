from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m, h = n - 1, n >> 1
        for i in range(h + 1):
            for j in range(i, m - i):
                (
                    matrix[i][j],
                    matrix[j][m - i],
                    matrix[m - i][m - j],
                    matrix[m - j][i],
                ) = (matrix[m - j][i], matrix[i][j], matrix[j][m - i], matrix[m - i][m - j])


def polyfill(matrix: List[List[int]]):
    Solution().rotate(matrix)
    print(matrix)


# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
polyfill(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
