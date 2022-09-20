from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxValue: int = nums[0]
        if len(nums) == 1:
            return maxValue

        res = maxValue
        for i in range(1, len(nums)):
            if maxValue <= 0:
                maxValue = nums[i]
            else:
                maxValue += nums[i]
            res = max(res, maxValue)

        return res


# 6
print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

# 23
print(Solution().maxSubArray([5, 4, -1, 7, 8]))
