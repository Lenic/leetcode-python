from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums) + 1
        prefixSum = left = right = 0
        while right <= len(nums):
            if prefixSum < target:
                if right < len(nums):
                    prefixSum += nums[right]
                right += 1
            else:
                ans = min(ans, right - left)
                prefixSum -= nums[left]
                left += 1
        return ans if ans <= len(nums) else 0


# 2
print(Solution().minSubArrayLen(target=15, nums=[5, 1, 3, 5, 10, 7, 4, 9, 2, 8]))

# 5
print(Solution().minSubArrayLen(target=15, nums=[1, 2, 3, 4, 5]))

# 2
print(Solution().minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))

# 3
print(Solution().minSubArrayLen(target=11, nums=[1, 2, 3, 4, 5]))

# 0
print(Solution().minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))

# 1
print(Solution().minSubArrayLen(target=4, nums=[1, 4, 4]))

# 2
print(Solution().minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
