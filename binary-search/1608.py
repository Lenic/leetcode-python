from typing import List


class Solution:
    def binarySearch(self, nums: List[int], targetValue: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] < targetValue:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums) + 1):
            index = self.binarySearch(nums, i)
            count = len(nums) - index
            if i == count:
                return i
        return -1


# 6
print(Solution().specialArray([3, 9, 7, 8, 3, 8, 6, 6]))

# -1
print(Solution().specialArray([3, 6, 7, 7, 0]))

# 3
print(Solution().specialArray([0, 4, 3, 0, 4]))

# 2
print(Solution().specialArray([3, 5]))

# -1
print(Solution().specialArray([0, 0]))
