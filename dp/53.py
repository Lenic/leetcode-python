from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = ans = nums[0]
        for i in range(1, len(nums)):
            prev = max(prev + nums[i], nums[i])
            ans = max(ans, prev)
        return ans


# -1
print(Solution().maxSubArray([-1]))

# 6
print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

# 23
print(Solution().maxSubArray([5, 4, -1, 7, 8]))
