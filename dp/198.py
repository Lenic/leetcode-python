from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        data = [0] * len(nums)
        data[0] = nums[0]
        data[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            data[i] = max(data[i - 2] + nums[i], data[i - 1])

        return data[-1]


# 4
print(Solution().rob([2, 1, 1, 2]))

# 4
print(Solution().rob([1, 2, 3, 1]))

# 12
print(Solution().rob([2, 7, 9, 3, 1]))
