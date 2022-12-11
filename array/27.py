from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left: int = -1
        for i, item in enumerate(nums):
            if item == val:
                left = i
                break
        if left == -1:
            return len(nums)
        for i in range(left + 1, len(nums)):
            if nums[i] != val:
                nums[left], left = nums[i], left + 1
        return left


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
