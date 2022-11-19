from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum, restSum = 0, sum(nums)
        for i, val in enumerate(nums):
            restSum -= val
            if prefixSum == restSum:
                return i
            prefixSum += val
        return -1


# 3
print(Solution().pivotIndex(nums=[1, 7, 3, 6, 5, 6]))

# 2
print(Solution().pivotIndex(nums=[-1, -1, -1, -1, -1, 0]))
