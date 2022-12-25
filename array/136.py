from typing import List

from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


# 1
print(Solution().singleNumber([1]))

# 4
print(Solution().singleNumber([4, 1, 2, 1, 2]))

# 1
print(Solution().singleNumber([2, 2, 1]))
