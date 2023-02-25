from typing import List
from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        left1 = left2 = right = 0
        sum1 = sum2 = 0
        ret = 0
        while right < n:
            sum1 += nums[right]
            while left1 <= right and sum1 > goal:
                sum1 -= nums[left1]
                left1 += 1
            sum2 += nums[right]
            while left2 <= right and sum2 >= goal:
                sum2 -= nums[left2]
                left2 += 1
            ret += left2 - left1
            right += 1
        return ret


# 4
print(Solution().numSubarraysWithSum(nums=[1, 0, 1, 0, 1], goal=2))

# 15
print(Solution().numSubarraysWithSum(nums=[0, 0, 0, 0, 0], goal=0))
