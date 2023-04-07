from typing import List
from sortedcontainers import SortedList


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = left = right = 0
        cache = SortedList[int]([])
        while right < len(nums):
            cache.add(nums[right])
            right += 1
            while cache[-1] - cache[0] > limit:
                cache.remove(nums[left])
                left += 1
            ans = max(ans, right - left)
        return ans


# 3
print(Solution().longestSubarray(nums=[4, 2, 2, 2, 4, 4, 2, 2], limit=0))

# 4
print(Solution().longestSubarray(nums=[10, 1, 2, 4, 7, 2], limit=5))

# 2
print(Solution().longestSubarray(nums=[8, 2, 4, 7], limit=4))
