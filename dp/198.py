from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        left = right = 0
        for val in nums:
            left, right = right, max(left + val, right)
        return right


# 4
print(Solution().rob([2, 1, 1, 2]))

# 4
print(Solution().rob([1, 2, 3, 1]))

# 12
print(Solution().rob([2, 7, 9, 3, 1]))
