from typing import Callable, List


class Solution:
    def binarySearch(
        self, data: List[int], target: int, left: int, right: int, comparer: Callable[[int, int], bool]
    ) -> int:
        while left <= right:
            mid = left + ((right - left) >> 1)
            if comparer(data[mid], target):
                right = mid - 1
            else:
                left = mid + 1
        return left

    def searchRight(self, data: List[int], target: int, left: int) -> int:
        index = self.binarySearch(data, target, left, len(data) - 1, lambda x, y: x > y)
        if index == len(data):
            return index - 1 if data[-1] == target else -1
        return index - 1 if data[index - 1] == target else -1

    def searchLeft(self, data: List[int], target: int) -> int:
        index = self.binarySearch(data, target, 0, len(data) - 1, lambda x, y: x >= y)
        if index == 0:
            return 0 if data[0] == target else -1
        elif index == len(data):
            return index - 1 if data[-1] == target else -1
        return index if data[index] == target else -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        empty = [-1, -1]
        if not len(nums):
            return empty

        left = self.searchLeft(nums, target)
        if left == -1:
            return empty
        right = self.searchRight(nums, target, left + 1)
        return [left, right]


# [4, 4]
print(Solution().searchRange([7, 7, 8, 8, 10], 10))

# [-1,-1]
print(Solution().searchRange([7, 7, 8, 8, 10], 12))

# [0,1]
print(Solution().searchRange([7, 7, 8, 8, 10], 7))

# [-1,-1]
print(Solution().searchRange([7, 7, 8, 8, 10], 6))

# [-1,-1]
print(Solution().searchRange([], 0))

# [-1,-1]
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))

# [3,4]
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
