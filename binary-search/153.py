from typing import List

from sys import maxsize


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res, left, right = maxsize, 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[left] <= nums[mid]:
                if res > nums[left]:
                    res = nums[left]
                left = mid + 1
            # nums[mid] <= nums[right]
            else:
                if res > nums[mid]:
                    res = nums[mid]
                right = mid - 1
        return res


# 1
print(Solution().findMin([5, 1, 2, 3, 4]))

# 11
print(Solution().findMin([11, 13, 15, 17]))

# 0
print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))

# 1
print(Solution().findMin([3, 4, 5, 1, 2]))
