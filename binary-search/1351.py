from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res, n = 0, len(grid[0])
        last = n
        for row in grid:
            left, right = 0, last - 1
            while left <= right:
                mid = left + ((right - left) >> 1)
                if row[mid] >= 0:
                    left = mid + 1
                else:
                    right = mid - 1
            res += n - left
            last = left
        return res


# 1
print(Solution().countNegatives([[3, 2], [1, -1]]))

# 0
print(Solution().countNegatives([[3, 2], [1, 0]]))

# 8
print(Solution().countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
