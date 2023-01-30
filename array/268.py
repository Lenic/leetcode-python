from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)
        for i in range(len(nums) + 1):
            if i not in s:
                return i
        return -1


# 2
print(Solution().missingNumber([3, 0, 1]))
