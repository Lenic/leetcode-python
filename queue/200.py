from typing import List

from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols, count = len(grid), len(grid[0]), 0
        visited = [[False] * cols for _ in range(rows)]

        targetValue: str = "1"
        cur: deque[tuple[int, int]] = deque([(0, 0)])
        next: deque[tuple[int, int, str]] = deque([])

        while True:
            isChanged: bool = False
            while cur:
                nextTargetValue = "0" if targetValue == "1" else "1"
                for _ in range(len(cur)):
                    row, col = cur.popleft()
                    if visited[row][col]:
                        continue
                    if grid[row][col] == targetValue:
                        isChanged = visited[row][col] = True
                    else:
                        next.append((row, col, nextTargetValue))
                        continue
                    if row - 1 >= 0 and not visited[row - 1][col]:
                        if grid[row - 1][col] == targetValue:
                            cur.append((row - 1, col))
                        else:
                            next.append((row - 1, col, nextTargetValue))
                    if row + 1 < rows and not visited[row + 1][col]:
                        if grid[row + 1][col] == targetValue:
                            cur.append((row + 1, col))
                        else:
                            next.append((row + 1, col, nextTargetValue))
                    if col - 1 >= 0 and not visited[row][col - 1]:
                        if grid[row][col - 1] == targetValue:
                            cur.append((row, col - 1))
                        else:
                            next.append((row, col - 1, nextTargetValue))
                    if col + 1 < cols and not visited[row][col + 1]:
                        if grid[row][col + 1] == targetValue:
                            cur.append((row, col + 1))
                        else:
                            next.append((row, col + 1, nextTargetValue))
            if targetValue == "1" and isChanged:
                count += 1
            if next:
                (c, r, targetValue) = next.popleft()
                cur.append((c, r))
            else:
                break
        return count


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
