from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        max = n - 1
        for i in range(n >> 1):
            for j in range(i, n - i - 1):
                (
                    matrix[i][j],
                    matrix[max - j][i],
                    matrix[max - i][max - j],
                    matrix[j][max - i],
                ) = (
                    matrix[max - j][i],
                    matrix[max - i][max - j],
                    matrix[j][max - i],
                    matrix[i][j],
                )


m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Solution().rotate(m1)
print(m1)
