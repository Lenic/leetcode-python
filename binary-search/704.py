from typing import List


class Solution:
    def binarySearch(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left > right:
            return -1

        mid = left + ((right - left) >> 1)
        if nums[mid] > target:
            return self.binarySearch(nums, target, left, mid - 1)
        elif nums[mid] < target:
            return self.binarySearch(nums, target, mid + 1, right)
        else:
            return mid

    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums) - 1)


# 0
print(Solution().search([5], 5))

# 4
print(Solution().search([-1, 0, 3, 5, 9, 12], 9))

# -1
print(Solution().search([-1, 0, 3, 5, 9, 12], 2))
