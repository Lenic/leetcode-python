from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        ans, left, maxIndex = 1, 0, len(nums) - 1
        right = min(nums[0], maxIndex)

        while right < maxIndex:
            maxPosition = left
            for i in range(left + 1, right + 1):
                maxPosition = max(maxPosition, i + nums[i])

            ans += 1
            left = right
            right = maxPosition

        return ans


# 3
print(Solution().jump([1, 1, 1, 1]))

# 2
print(Solution().jump([1, 2, 3]))

# 2
print(Solution().jump([2, 3, 1, 1, 4]))

# 2
print(Solution().jump([2, 3, 0, 1, 4]))
