from typing import List

from collections import deque


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        q: deque[int] = deque([])
        for i, item in enumerate(nums):
            if item == val:
                q.append(i)
        ans = len(nums) - len(q)
        for i in range(len(nums) - 1, -1, -1):
            if not len(q):
                break
            if nums[i] != val:
                nums[q.popleft()] = nums[i]
        return ans


def polyfill(nums: List[int], val: int):
    n = Solution().removeElement(nums, val)
    print(n, nums[:n])


# 1, [2]
polyfill(nums=[2], val=3)

# 0, []
polyfill(nums=[], val=0)

# 2, [2,2]
polyfill(nums=[3, 2, 2, 3], val=3)

# 5 [0,1,4,0,3]
polyfill(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2)
