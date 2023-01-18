from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        v0 = v1 = v2 = 0
        for val in nums:
            v0, v1, v2 = v1, v2, max(v0 + val, v1 + val, v2)
        return v2


# 4
print(Solution().rob([2, 1, 1, 2]))

# 4
print(Solution().rob([1, 2, 3, 1]))

# 12
print(Solution().rob([2, 7, 9, 3, 1]))
