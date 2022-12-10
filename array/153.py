from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]


# 11
print(Solution().findMin(nums=[11, 13, 15, 17]))

# 0
print(Solution().findMin(nums=[4, 5, 6, 7, 0, 1, 2]))

# 1
print(Solution().findMin(nums=[3, 4, 5, 1, 2]))
