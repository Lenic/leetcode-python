from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur = 0
        for i in range(k):
            cur += nums[i]
        ans = cur
        for i in range(len(nums) - k):
            cur += nums[i + k] - nums[i]
            ans = max(ans, cur)
        return ans / k


# 12.75
print(Solution().findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4))

# 5
print(Solution().findMaxAverage(nums=[5], k=1))
