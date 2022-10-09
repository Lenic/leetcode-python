from typing import Callable, List, TypeVar

T = TypeVar("T")


class Solution:
    def binarySearch(self, data: List[T], comparer: Callable[[T], int]) -> int:
        ans, left, right = 0, 0, len(data) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if comparer(data[mid]) <= 0:
                left = mid + 1
                ans = mid
            else:
                right = mid - 1
        return ans

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.binarySearch(matrix, lambda x: x[0] - target)
        index = self.binarySearch(matrix[row], lambda x: x - target)
        if matrix[row][index] != target:
            if row > 0:
                index = self.binarySearch(matrix[row - 1], lambda x: x - target)
                return False if matrix[row - 1][index] != target else True
            else:
                return False
        return True


# True
print(Solution().searchMatrix([[1, 3, 15, 17], [10, 11, 16, 20], [23, 30, 34, 60]], 15))

# True
print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))

# False
print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))

# True
print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 20))
