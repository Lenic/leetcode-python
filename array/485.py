from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = -1
        for i, val in enumerate(nums):
            if val == 1:
                left = i
                break
        if left == -1:
            return 0
        ans = -1
        for i in range(left + 1, len(nums)):
            val = nums[i]
            if val != 1:
                ans = max(ans, i - left)
                left = i
            elif nums[left] != 1:
                left = i
        if nums[left] == 1:
            ans = max(ans, len(nums) - left)
        return ans if ans != -1 else 0


# 2
print(Solution().findMaxConsecutiveOnes(nums=[1, 0, 1, 1, 0, 1]))

# 3
print(Solution().findMaxConsecutiveOnes(nums=[1, 1, 0, 1, 1, 1]))
