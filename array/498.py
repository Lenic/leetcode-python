from typing import Generator, List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        total, forward = m * n, True

        def getNext(i: int, j: int) -> tuple[int, int]:
            nonlocal forward
            if not ((i == 0 or j == n - 1) if forward else (j == 0 or i == m - 1)):
                return (i - 1, j + 1) if forward else (i + 1, j - 1)
            else:
                forward = not forward
                if not forward:
                    return (i, j + 1) if j < n - 1 else (i + 1, j)
                else:
                    return (i + 1, j) if i != m - 1 else (i, j + 1)

        i = j = 0
        ans: List[int] = []
        while True:
            ans.append(mat[i][j])
            if len(ans) == total:
                break
            i, j = getNext(i, j)
        return ans


# [1,2,4,5,3,6]
print(Solution().findDiagonalOrder(mat=[[1, 2, 3], [4, 5, 6]]))

# [1,2,4,7,5,3,6,8,9]
print(Solution().findDiagonalOrder(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# [1,2,3,4]
print(Solution().findDiagonalOrder(mat=[[1, 2], [3, 4]]))
