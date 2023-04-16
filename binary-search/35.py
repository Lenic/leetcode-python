from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left


# 4
print(Solution().searchInsert([1, 3, 5, 6], 7))

# 1
print(Solution().searchInsert([1, 3, 5, 6], 2))

# 2
print(Solution().searchInsert([1, 3, 5, 6], 5))
