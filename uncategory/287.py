from typing import List

import heapq


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                break
        return slow


# 2
print(Solution().findDuplicate([2, 2, 2, 2, 2]))

# 2
print(Solution().findDuplicate([1, 3, 4, 2, 2]))

# 3
print(Solution().findDuplicate([3, 1, 3, 4, 2]))
