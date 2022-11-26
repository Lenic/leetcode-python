from typing import Generator, List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans: List[int] = []
        m, n = len(mat), len(mat[0])
        total, forward, mmax, nmax = m * n, True, m - 1, n - 1

        def getNext(i: int, j: int) -> tuple[int, int]:
            isEdge = False
            nonlocal forward
            if forward:
                isEdge = i == 0 or j == nmax
            else:
                isEdge = j == 0 or i == mmax
            if not isEdge:
                return (i - 1, j + 1) if forward else (i + 1, j - 1)
            else:
                # 首先将方向反向，所以后面的判断是相反的
                forward = not forward
                # 因为方向，所以此处 i 肯定是等于 0 的。接下来只需要判断 j 的值即可，如果 i != 0，那么就肯定是最后一个元素
                if not forward:
                    if j < nmax:
                        return (i, j + 1)
                    else:
                        return (i + 1, j)
                # 区分 i 是否等于 mmax
                else:
                    if i != mmax:
                        return (i + 1, j)
                    else:
                        return (i, j + 1)

        i = j = 0
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
