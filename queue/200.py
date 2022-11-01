from typing import List

from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        gr, gc, res = len(grid), len(grid[0]), 0
        for r in range(gr):
            for c in range(gc):
                if grid[r][c] == "1":
                    res += 1
                    grid[r][c] = "0"
                    neighbors = deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < gr and 0 <= y < gc and grid[x][y] == "1":
                                grid[x][y] = "0"
                                neighbors.append((x, y))
        return res


# 4
print(Solution().numIslands(grid=[["0", "1", "0"], ["1", "0", "1"], ["0", "1", "0"]]))

# 0
print(Solution().numIslands(grid=[["0"]]))

# 3
print(
    Solution().numIslands(
        grid=[
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)

# 1
print(
    Solution().numIslands(
        grid=[
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)
