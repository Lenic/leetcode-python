from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, column = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * column for _ in range(row)]
        for i in range(row):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for i in range(column):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1

        for i in range(1, row):
            for j in range(1, column):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


# 2
print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
