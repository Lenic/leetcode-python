from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def search(data: List[int], left: int, right: int) -> int:
            while left <= right:
                mid = left + ((right - left) >> 1)
                if data[mid] >= 0:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        ans, n = [], len(grid[0])
        for val in grid:
            ans.append(search(val, 0, (ans[-1] if len(ans) else n) - 1))
        return sum(n - val for val in ans)


# 1
print(Solution().countNegatives([[3, 2], [1, -1]]))

# 0
print(Solution().countNegatives([[3, 2], [1, 0]]))

# 8
print(Solution().countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
