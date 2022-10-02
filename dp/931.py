from typing import List

from sys import maxsize


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        ans = matrix[0][:]
        for i in range(1, n):
            next = [maxsize] * n
            for j in range(n):
                for k in range(max(j - 1, 0), min(j + 2, n)):
                    next[k] = min(next[k], ans[j] + matrix[i][k])
            ans = next
        return min(ans)


# 8
print(Solution().minFallingPathSum([[1, 2, 3, 4], [6, 6, 6, 6], [7, 8, 9, -1], [1, 1, 1, 1]]))

# -36
print(Solution().minFallingPathSum([[100, -42, -46, -41], [31, 97, 10, -10], [-58, -51, 82, 89], [51, 81, 69, -51]]))

# 13
print(Solution().minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
