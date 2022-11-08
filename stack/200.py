from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        trs, tcs, ans = len(grid), len(grid[0]), 0

        def dfs(x: int, y: int):
            if grid[x][y] == "0":
                return
            grid[x][y] = "0"
            for a, b in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= a < trs and 0 <= b < tcs:
                    dfs(a, b)

        for i in range(trs):
            for j in range(tcs):
                if grid[i][j] == "0":
                    continue
                ans += 1
                dfs(i, j)
        return ans


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
