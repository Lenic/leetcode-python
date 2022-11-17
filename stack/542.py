from typing import Generator, List

from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        ans: List[List[int]] = [[-1] * cols for _ in range(rows)]

        q: deque[tuple[int, int]] = deque([])
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    q.append((i, j))

        def bfs(i: int, j: int) -> Generator[tuple[int, int], None, None]:
            if i - 1 >= 0 and ans[i - 1][j] == -1:
                yield (i - 1, j)
            if i + 1 < rows and ans[i + 1][j] == -1:
                yield (i + 1, j)
            if j - 1 >= 0 and ans[i][j - 1] == -1:
                yield (i, j - 1)
            if j + 1 < cols and ans[i][j + 1] == -1:
                yield (i, j + 1)

        distance: int = 0
        while q:
            distance += 1
            for _ in range(len(q)):
                horizontal, vertical = q.popleft()
                for i, j in bfs(horizontal, vertical):
                    ans[i][j] = distance
                    q.append((i, j))
        return ans


# [[0,0,0],[0,1,0],[1,2,1]]
print(Solution().updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]]))

# [[0,0,0],[0,1,0],[0,0,0]]
print(Solution().updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
