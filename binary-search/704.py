from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1


# 0
print(Solution().search([5], 5))

# 4
print(Solution().search([-1, 0, 3, 5, 9, 12], 9))

# -1
print(Solution().search([-1, 0, 3, 5, 9, 12], 2))
