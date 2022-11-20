from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


# 2
print(Solution().searchInsert(nums=[1, 3, 5, 6], target=5))

# 1
print(Solution().searchInsert(nums=[1, 3, 5, 6], target=2))

# 4
print(Solution().searchInsert(nums=[1, 3, 5, 6], target=7))
