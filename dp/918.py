from typing import List

from sys import maxsize


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        maxValue = -maxsize
        # 无环
        pre = 0
        for i in range(n):
            pre = max(0, pre) + nums[i]
            maxValue = max(maxValue, pre)
        # 如果最子数组和小于0，说明数组中全为负数，返回最大负数即可
        if maxValue < 0:
            return maxValue
        # 有环
        pre = 0
        minValue = maxsize
        for i in range(n):
            pre = min(0, pre) + nums[i]
            minValue = min(minValue, pre)
        # 因为不知道最大子数组的位置，所以需要从两种情况中取最大值
        return max(maxValue, sum(nums) - minValue)


# 15
print(Solution().maxSubarraySumCircular([-2, 4, -5, 4, -5, 9, 4]))

# 3
print(Solution().maxSubarraySumCircular([1, -2, 3, -2]))

# 10
print(Solution().maxSubarraySumCircular([5, -3, 5]))
