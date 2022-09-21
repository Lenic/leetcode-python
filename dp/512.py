from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = minValue = maxValue = nums[0]
        for i in range(1, len(nums)):
            item, previousMin, previousMax = nums[i], minValue, maxValue

            maxValue = max(previousMax * item, max(item, item * previousMin))
            minValue = min(previousMin * item, min(item, item * previousMax))
            res = max(res, maxValue)
        return res


# -2
print(Solution().maxProduct([-2]))

# 24
print(Solution().maxProduct([-2, 3, -4]))

# 2
print(Solution().maxProduct([0, 2]))

# 6
print(Solution().maxProduct([2, 3, -2, 4]))

# 3
print(Solution().maxProduct([-2, 0, -1, -3]))
