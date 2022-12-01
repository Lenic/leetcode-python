from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = ans = 0
        while i < len(nums):
            ans += nums[i]
            i += 2
        return ans


# 2
print(Solution().arrayPairSum(nums=[1, 4, 3, 2]))
