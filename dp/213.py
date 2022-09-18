from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(i: int, j: int):
            left, right = nums[i], max(nums[i], nums[i + 1])
            for index in range(i + 2, j + 1):
                left, right = right, max(left + nums[index], right)
            return right

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        return max(dp(0, len(nums) - 2), dp(1, len(nums) - 1))


# 2
print(Solution().rob([2]))

# 3
print(Solution().rob([2, 3, 2]))

# 4
print(Solution().rob([1, 2, 3, 1]))
