from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        left, right = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            left, right = right, max(left + nums[i], right)
        return right


# 4
print(Solution().rob([2, 1, 1, 2]))

# 4
print(Solution().rob([1, 2, 3, 1]))

# 12
print(Solution().rob([2, 7, 9, 3, 1]))
