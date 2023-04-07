from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans, n = 0, len(nums)
        for left in range(n):
            right = left
            minValue = maxValue = nums[left]
            while right < n - 1:
                cur = nums[right + 1]
                if abs(minValue - cur) <= limit and abs(maxValue - cur) <= limit:
                    if cur < minValue:
                        minValue = cur
                    if cur > maxValue:
                        maxValue = cur
                    right += 1
                else:
                    break
            ans = max(ans, right - left + 1)
        return ans


# 3
print(Solution().longestSubarray(nums=[4, 2, 2, 2, 4, 4, 2, 2], limit=0))

# 4
print(Solution().longestSubarray(nums=[10, 1, 2, 4, 7, 2], limit=5))

# 2
print(Solution().longestSubarray(nums=[8, 2, 4, 7], limit=4))
