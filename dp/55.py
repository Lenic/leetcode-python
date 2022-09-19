from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        val, maxValue = 0, len(nums) - 1
        for i in range(len(nums)):
            if val < i:
                return False
            val = max(val, i + nums[i])
            if val >= maxValue:
                return True
        return False


# True
print(Solution().canJump([0]))

# False
print(Solution().canJump([0, 2, 3]))

# True
print(Solution().canJump([4, 0, 0, 0, 4]))

# True
print(Solution().canJump([2, 3, 1, 1, 4]))

# False
print(Solution().canJump([3, 2, 1, 0, 4]))
