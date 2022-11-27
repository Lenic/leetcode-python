from typing import Generator, List

from collections import deque


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ans, m, n = 0, len(grid), len(grid[0])
        if m <= 2 or n <= 2:
            return 0

        def getNeighbors(x: int, y: int) -> Generator[tuple[int, int], None, None]:
            if x - 1 >= 0 and grid[x - 1][y] == 0:
                yield (x - 1, y)
            if x + 1 < m and grid[x + 1][y] == 0:
                yield (x + 1, y)
            if y - 1 >= 0 and grid[x][y - 1] == 0:
                yield (x, y - 1)
            if y + 1 < n and grid[x][y + 1] == 0:
                yield (x, y + 1)

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                val = grid[i][j]
                if val == 1:
                    continue
                isIsland, q = True, deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    grid[x][y] = 1
                    isEdge = x == 0 or y == 0 or x == m - 1 or y == n - 1
                    if isEdge:
                        isIsland = False
                    q.extend(getNeighbors(x, y))
                if isIsland:
                    ans += 1
        return ans


# 2
print(
    Solution().closedIsland(
        grid=[
            [1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0],
        ]
    )
)
